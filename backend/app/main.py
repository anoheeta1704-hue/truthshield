from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import health, analyze
from app.config import settings

app = FastAPI(
    title="TruthShield API",
    description="AI-based audio deception analysis system",
    version="0.1.0",
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins_list,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routers
app.include_router(health.router, tags=["health"])
app.include_router(analyze.router, prefix="/analyze", tags=["analyze"])

# Stubs for future milestones
# app.include_router(sessions.router, prefix="/sessions", tags=["sessions"])
# app.include_router(stream.router, prefix="/stream", tags=["stream"])
