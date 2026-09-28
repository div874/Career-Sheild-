from typing import List, Optional
from pydantic import BaseModel, Field


class Education(BaseModel):
    institution: str
    degree: str
    field_of_study: Optional[str] = None
    start_year: Optional[int] = None
    end_year: Optional[int] = None
    grade_gpa: Optional[str] = None


class Experience(BaseModel):
    title: str
    company: str
    location: Optional[str] = None
    start_date: Optional[str] = None
    end_date: Optional[str] = None
    is_current: bool = False
    description: List[str] = Field(default_factory=list)


class CareerPreferences(BaseModel):
    target_roles: List[str] = Field(default_factory=list)
    preferred_locations: List[str] = Field(default_factory=list)
    work_types: List[str] = Field(default_factory=list)  # e.g., Internship, Full-time, Remote
    min_stipend_salary: Optional[float] = None
    preferred_technologies: List[str] = Field(default_factory=list)


class CandidateProfile(BaseModel):
    name: str
    email: Optional[str] = None
    phone: Optional[str] = None
    location: Optional[str] = None
    summary: Optional[str] = None
    skills: List[str] = Field(default_factory=list)
    programming_languages: List[str] = Field(default_factory=list)
    frameworks_tools: List[str] = Field(default_factory=list)
    education: List[Education] = Field(default_factory=list)
    experiences: List[Experience] = Field(default_factory=list)
    certifications: List[str] = Field(default_factory=list)
    experience_level: str = "Student"  # e.g., Student, Entry-Level, Mid-Level
    preferences: Optional[CareerPreferences] = None
