from fastapi import APIRouter, Depends, Request
from app.middleware.auth import auth_required, optional_auth
from typing import Dict, Any

router = APIRouter(prefix="/auth", tags=["authentication"])


@router.get("/me")
async def get_current_user(request: Request, token_payload: Dict[str, Any] = Depends(auth_required)):
    """Get current authenticated user information"""
    return {
        "user": request.state.user,
        "token_info": {
            "issued_at": token_payload.get("iat"),
            "expires_at": token_payload.get("exp"),
        }
    }


@router.get("/verify")
async def verify_token(token_payload: Dict[str, Any] = Depends(auth_required)):
    """Verify if token is valid"""
    return {"valid": True, "user_id": token_payload.get("sub")}


@router.get("/check")
async def check_auth(token_payload: Dict[str, Any] = Depends(optional_auth)):
    """Check authentication status (doesn't require auth)"""
    if token_payload:
        return {"authenticated": True, "user_id": token_payload.get("sub")}
    return {"authenticated": False}