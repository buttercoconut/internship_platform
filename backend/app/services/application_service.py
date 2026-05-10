"""Service layer for application approval logic."""

from sqlalchemy.orm import Session
from datetime import datetime

from ..models.models import Application


def approve_application(db: Session, application_id: int) -> Application:
    """Approve an internship application.

    Args:
        db: SQLAlchemy session.
        application_id: ID of the application to approve.

    Returns:
        The updated Application object.

    Raises:
        ValueError: If the application does not exist or is already approved.
    """
    application = db.query(Application).filter(Application.id == application_id).first()
    if not application:
        raise ValueError(f"Application {application_id} not found")
    if application.status == "approved":
        raise ValueError(f"Application {application_id} already approved")
    application.status = "approved"
    application.approved_at = datetime.utcnow()
    db.commit()
    db.refresh(application)
    return application
