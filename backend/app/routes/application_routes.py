"""FastAPI router for application endpoints."""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from ..database.db import get_db
from ..schemas.schemas import ApplicationCreateSchema, ApplicationSchema
from ..services.application_service import approve_application

router = APIRouter(prefix="/applications", tags=["applications"])

@router.post("/", response_model=ApplicationSchema)
async def create_application(app_in: ApplicationCreateSchema, db: Session = Depends(get_db)):
    # Simplified creation logic – in a real system you would validate student and internship existence
    from ..models.models import Application
    application = Application(**app_in.dict())
    db.add(application)
    db.commit()
    db.refresh(application)
    return application

@router.post("/{application_id}/approve", response_model=ApplicationSchema)
async def approve(app_id: int, db: Session = Depends(get_db)):
    try:
        application = approve_application(db, app_id)
    except ValueError as exc:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(exc))
    return application
