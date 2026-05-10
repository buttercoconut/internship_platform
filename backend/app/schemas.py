from pydantic import BaseModel, EmailStr, Field
from typing import List, Optional
from datetime import datetime

# ---------- Student Schemas ----------
class StudentBase(BaseModel):
    name: str
    email: EmailStr

class StudentCreate(StudentBase):
    password: str

class Student(StudentBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True

# ---------- Company Schemas ----------
class CompanyBase(BaseModel):
    name: str
    email: EmailStr
    address: Optional[str] = None

class CompanyCreate(CompanyBase):
    password: str

class Company(CompanyBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True

# ---------- Internship Posting Schemas ----------
class InternshipPostingBase(BaseModel):
    title: str
    description: Optional[str] = None
    location: Optional[str] = None
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None

class InternshipPostingCreate(InternshipPostingBase):
    company_id: int

class InternshipPosting(InternshipPostingBase):
    id: int
    company_id: int
    created_at: datetime

    class Config:
        orm_mode = True

# ---------- Application Schemas ----------
class ApplicationBase(BaseModel):
    status: Optional[str] = "pending"

class ApplicationCreate(ApplicationBase):
    student_id: int
    posting_id: int

class Application(ApplicationBase):
    id: int
    student_id: int
    posting_id: int
    applied_at: datetime

    class Config:
        orm_mode = True
