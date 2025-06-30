from fastapi import HTTPException, Request, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import jwt, jwk, JWTError
from jose.utils import base64url_decode
import httpx
import json
from typing import Optional, Dict, Any
import time
from app.core.config import settings


class ClerkJWTVerifier:
    def __init__(self):
        self.jwks_url = settings.CLERK_JWKS_URL
        self.jwks_cache = None
        self.jwks_cache_time = 0
        self.cache_duration = 3600  # 1 hour
        
    async def get_jwks(self) -> Dict[str, Any]:
        """Fetch JWKS from Clerk with caching"""
        current_time = time.time()
        
        if self.jwks_cache and (current_time - self.jwks_cache_time) < self.cache_duration:
            return self.jwks_cache
            
        async with httpx.AsyncClient() as client:
            response = await client.get(self.jwks_url)
            response.raise_for_status()
            self.jwks_cache = response.json()
            self.jwks_cache_time = current_time
            return self.jwks_cache
    
    async def verify_token(self, token: str) -> Dict[str, Any]:
        """Verify JWT token from Clerk"""
        try:
            # Decode token header to get kid
            header = jwt.get_unverified_header(token)
            kid = header.get("kid")
            
            if not kid:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Invalid token: No kid in header"
                )
            
            # Get JWKS
            jwks = await self.get_jwks()
            
            # Find the key with matching kid
            key = None
            for k in jwks.get("keys", []):
                if k.get("kid") == kid:
                    key = k
                    break
            
            if not key:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Invalid token: Key not found"
                )
            
            # Verify and decode token
            public_key = jwk.construct(key)
            payload = jwt.decode(
                token,
                public_key,
                algorithms=["RS256"],
                options={"verify_aud": False}  # Clerk doesn't always set audience
            )
            
            # Verify token is not expired
            if payload.get("exp", 0) < time.time():
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Token expired"
                )
            
            return payload
            
        except JWTError as e:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail=f"Invalid token: {str(e)}"
            )
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail=f"Token verification failed: {str(e)}"
            )


class ClerkAuthBearer(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super(ClerkAuthBearer, self).__init__(auto_error=auto_error)
        self.verifier = ClerkJWTVerifier()
        
    async def __call__(self, request: Request) -> Optional[Dict[str, Any]]:
        credentials: HTTPAuthorizationCredentials = await super(ClerkAuthBearer, self).__call__(request)
        
        if credentials:
            if not credentials.scheme == "Bearer":
                raise HTTPException(
                    status_code=status.HTTP_403_FORBIDDEN,
                    detail="Invalid authentication scheme."
                )
            
            # Verify token
            payload = await self.verifier.verify_token(credentials.credentials)
            
            # Add user info to request state
            request.state.user = {
                "id": payload.get("sub"),
                "email": payload.get("email"),
                "metadata": payload.get("metadata", {}),
                "session_id": payload.get("sid"),
            }
            
            return payload
        else:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Invalid authorization code."
            )


# Initialize auth dependency
auth_required = ClerkAuthBearer()


# Optional auth dependency (doesn't require auth but adds user info if available)
class OptionalClerkAuth(ClerkAuthBearer):
    def __init__(self):
        super().__init__(auto_error=False)
        
    async def __call__(self, request: Request) -> Optional[Dict[str, Any]]:
        try:
            return await super().__call__(request)
        except:
            return None


optional_auth = OptionalClerkAuth()