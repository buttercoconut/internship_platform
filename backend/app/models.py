from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime, Text
from sqlalchemy.orm import relationship
from datetime import datetime
from .database import Base

class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    # Relationships
    applications = relationship("Application", back_populates="student")

class Company(Base):
    __tablename__ = "companies"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    address = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    # Relationships
    postings = relationship("InternshipPosting", back_populates="company")

class InternshipPosting(Base):
    __tablename__ = "internship_postings"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(Text)
    location = Column(String)
    start_date = Column(DateTime)
    end_date = Column(DateTime)
    company_id = Column(Integer, ForeignKey("companies.id"))
    created_at = Column(DateTime, default=datetime.utcnow)
    # Relationships
    company = relationship("Company", back_populates="postings")
    applications = relationship("Application", back_populates="posting")

class Application(Base):
    __tablename__ = "applications"
    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("students.id"))
    posting_id = Column(Integer, ForeignKey("internship_postings.id"))
    status = Column(String, default="pending")  # pending, approved, rejected
    applied_at = Column(DateTime, default=datetime.utcnow)
    # Relationships
    student = relationship("Student", back_populates="applications")
    posting = relationship("InternshipPosting", back_populates="applications")

# Create tables (for dev only)
# from .database import engine
# Base.metadata.create_all(bind=engine)
