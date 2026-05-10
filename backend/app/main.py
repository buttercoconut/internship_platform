# FastAPI main entry point
from fastapi import FastAPI
from app.routes import internship

app = FastAPI(title="Internship Platform API")

# Include routers
app.include_router(internship.router, prefix="/api/internship", tags=["internship"])

# Root endpoint
@app.get("/")
async def root():
    return {"message": "Welcome to the Internship Platform API"}
