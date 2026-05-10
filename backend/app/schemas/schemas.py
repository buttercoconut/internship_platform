"""Pydantic schemas for API requests and responses."""

from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import List, Optional

# Student schemas
class StudentCreateSchema(BaseModel):
    name: str
    email: EmailStr
    phone: Optional[str] = None
    password: str

class StudentSchema(BaseModel):
    id: int
    name: str
    email: EmailStr
    phone: Optional[str] = None
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

# Company schemas
class CompanyCreateSchema(BaseModel):
    name: str
    email: EmailStr
    address: Optional[str] = None
    password: str

class CompanySchema(BaseModel):
    id: int
    name: str
    email: EmailStr
    address: Optional[str] = None
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

# InternshipPosting schemas
class InternshipPostingCreateSchema(BaseModel):
    title: str
    description: str
    location: str
    company_id: int
    start_date: datetime
    end_date: datetime
    stipend: Optional[float] = None

class InternshipPostingSchema(BaseModel):
    id: int
    title: str
    description: str
    location: str
    company_id: int
    start_date: datetime
    end_date: datetime
    stipend: Optional[float] = None
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

# Application schemas
class ApplicationCreateSchema(BaseModel):
    student_id: int
    internship_id: int
    status: str = "pending"

class ApplicationSchema(BaseModel):
    id: int
    student_id: int
    internship_id: int
    status: str
    applied_at: datetime
    approved_at: Optional[datetime] = None

    class Config:
        orm_mode = True

# Review schemas
class ReviewCreateSchema(BaseModel):
    student_id: int
    internship_id: int
    rating: int
    comment: Optional[str] = None

class ReviewSchema(BaseModel):
    id: int
    student_id: int
    internship_id: int
    rating: int
    comment: Optional[str] = None
    created_at: datetime

    class Config:
        orm_mode = True
