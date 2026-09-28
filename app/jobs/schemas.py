from typing import List, Optional
from enum import Enum
from pydantic import BaseModel, Field


class WorkType(str, Enum):
    INTERNSHIP = "Internship"
    FULL_TIME = "Full-time"
    PART_TIME = "Part-time"
    CONTRACT = "Contract"


class LocationType(str, Enum):
    REMOTE = "Remote"
    HYBRID = "Hybrid"
    ON_SITE = "On-site"


class Job(BaseModel):
    id: str
    title: str
    company: str
    description: str
    required_skills: List[str] = Field(default_factory=list)
    preferred_skills: List[str] = Field(default_factory=list)
    location: str
    location_type: LocationType = LocationType.ON_SITE
    work_type: WorkType = WorkType.INTERNSHIP
    experience_level: str = "Student"
    stipend_salary: Optional[str] = None
    posted_date: Optional[str] = None
    application_url: Optional[str] = None
    company_url: Optional[str] = None
    source: str = "Dataset"
    is_suspicious_flag: bool = False
    suspicious_reasons: List[str] = Field(default_factory=list)
