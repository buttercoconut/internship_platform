"""Pydantic models for database entities."""

from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

class StudentBase(BaseModel):
    name: str
    email: EmailStr
    phone: Optional[str] = None

class StudentCreate(StudentBase):
    password: str

class Student(StudentBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

class CompanyBase(BaseModel):
    name: str
    email: EmailStr
    address: Optional[str] = None

class CompanyCreate(CompanyBase):
    password: str

class Company(CompanyBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

class InternshipPostingBase(BaseModel):
    title: str
    description: str
    location: str
    company_id: int
    start_date: datetime
    end_date: datetime
    stipend: Optional[float] = None

class InternshipPostingCreate(InternshipPostingBase):
    pass

class InternshipPosting(InternshipPostingBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

class ApplicationBase(BaseModel):
    student_id: int
    internship_id: int
    status: str = "pending"
    applied_at: datetime = datetime.utcnow()

class ApplicationCreate(ApplicationBase):
    pass

class Application(ApplicationBase):
    id: int
    approved_at: Optional[datetime] = None

    class Config:
        orm_mode = True

class ReviewBase(BaseModel):
    student_id: int
    internship_id: int
    rating: int
    comment: Optional[str] = None

class ReviewCreate(ReviewBase):
    pass

class Review(ReviewBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
