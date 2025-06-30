from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.api import auth, menu, orders
import logging

# Configure logging
logging.basicConfig(level=getattr(logging, settings.LOG_LEVEL))
logger = logging.getLogger(__name__)

app = FastAPI(
    title=settings.PROJECT_NAME,
    description="A restaurant management platform API",
    version=settings.VERSION,
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins_list,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth.router, prefix=settings.API_PREFIX)
app.include_router(menu.router, prefix=settings.API_PREFIX)
app.include_router(orders.router, prefix=settings.API_PREFIX)

@app.get("/")
async def root():
    return {
        "message": "Restaurant API is running",
        "version": settings.VERSION,
        "docs": "/docs",
        "api_prefix": settings.API_PREFIX
    }

@app.get("/health")
async def health_check():
    return {"status": "healthy", "service": "restaurant-api"}

@app.get(f"{settings.API_PREFIX}/health")
async def api_health_check():
    return {"status": "healthy", "version": settings.VERSION}

@app.on_event("startup")
async def startup_event():
    logger.info(f"Starting {settings.PROJECT_NAME} v{settings.VERSION}")
    logger.info(f"API available at {settings.API_PREFIX}")
    logger.info(f"Clerk JWKS URL: {settings.CLERK_JWKS_URL}")
    logger.info(f"CORS Origins: {settings.cors_origins_list}")
    logger.info(f"Server running on http://{settings.HOST}:{settings.PORT}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=True,
        log_level=settings.LOG_LEVEL.lower()
    )