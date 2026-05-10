"""FastAPI application entry point."""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Import routers
from .routes.application_routes import router as application_router

# Create FastAPI instance
app = FastAPI(
    title="Internship Platform API",
    description="API for managing internship applications, approvals, and reviews.",
    version="0.1.0",
)

# Allow CORS for frontend development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production restrict this
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(application_router)

# Root endpoint
@app.get("/")
async def root():
    return {"message": "Welcome to the Internship Platform API"}
