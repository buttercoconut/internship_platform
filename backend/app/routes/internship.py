from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.database.database import get_db
from app import models, schemas

router = APIRouter()

# ---------- Student Endpoints ----------
@router.post("/students", response_model=schemas.Student, status_code=status.HTTP_201_CREATED)
def create_student(student: schemas.StudentCreate, db: Session = Depends(get_db)):
    db_student = models.Student(name=student.name, email=student.email, hashed_password=student.password)
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

@router.get("/students/{student_id}", response_model=schemas.Student)
def read_student(student_id: int, db: Session = Depends(get_db)):
    student = db.query(models.Student).filter(models.Student.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

# ---------- Company Endpoints ----------
@router.post("/companies", response_model=schemas.Company, status_code=status.HTTP_201_CREATED)
def create_company(company: schemas.CompanyCreate, db: Session = Depends(get_db)):
    db_company = models.Company(name=company.name, email=company.email, address=company.address, hashed_password=company.password)
    db.add(db_company)
    db.commit()
    db.refresh(db_company)
    return db_company

@router.get("/companies/{company_id}", response_model=schemas.Company)
def read_company(company_id: int, db: Session = Depends(get_db)):
    company = db.query(models.Company).filter(models.Company.id == company_id).first()
    if not company:
        raise HTTPException(status_code=404, detail="Company not found")
    return company

# ---------- Internship Posting Endpoints ----------
@router.post("/postings", response_model=schemas.InternshipPosting, status_code=status.HTTP_201_CREATED)
def create_posting(posting: schemas.InternshipPostingCreate, db: Session = Depends(get_db)):
    db_posting = models.InternshipPosting(**posting.dict())
    db.add(db_posting)
    db.commit()
    db.refresh(db_posting)
    return db_posting

@router.get("/postings/{posting_id}", response_model=schemas.InternshipPosting)
def read_posting(posting_id: int, db: Session = Depends(get_db)):
    posting = db.query(models.InternshipPosting).filter(models.InternshipPosting.id == posting_id).first()
    if not posting:
        raise HTTPException(status_code=404, detail="Posting not found")
    return posting

@router.get("/postings", response_model=List[schemas.InternshipPosting])
def list_postings(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    postings = db.query(models.InternshipPosting).offset(skip).limit(limit).all()
    return postings

# ---------- Application Endpoints ----------
@router.post("/applications", response_model=schemas.Application, status_code=status.HTTP_201_CREATED)
def create_application(application: schemas.ApplicationCreate, db: Session = Depends(get_db)):
    db_application = models.Application(**application.dict())
    db.add(db_application)
    db.commit()
    db.refresh(db_application)
    return db_application

@router.get("/applications/{application_id}", response_model=schemas.Application)
def read_application(application_id: int, db: Session = Depends(get_db)):
    application = db.query(models.Application).filter(models.Application.id == application_id).first()
    if not application:
        raise HTTPException(status_code=404, detail="Application not found")
    return application

@router.get("/applications", response_model=List[schemas.Application])
def list_applications(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    applications = db.query(models.Application).offset(skip).limit(limit).all()
    return applications
