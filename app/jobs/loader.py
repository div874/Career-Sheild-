import csv
import json
from pathlib import Path
from typing import List, Union
from app.jobs.schemas import Job, WorkType, LocationType


def load_jobs_from_csv(file_path: Union[str, Path]) -> List[Job]:
    """Loads job postings from a CSV file into a list of Job objects."""
    jobs: List[Job] = []
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"Job dataset file not found at: {file_path}")

    with open(path, mode="r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Parse skills lists from string (comma or pipe separated)
            req_skills = [s.strip() for s in row.get("required_skills", "").split("|") if s.strip()]
            pref_skills = [s.strip() for s in row.get("preferred_skills", "").split("|") if s.strip()]
            suspicious_reasons = [r.strip() for r in row.get("suspicious_reasons", "").split("|") if r.strip()]

            # Determine enum values safely
            try:
                location_type = LocationType(row.get("location_type", "On-site"))
            except ValueError:
                location_type = LocationType.ON_SITE

            try:
                work_type = WorkType(row.get("work_type", "Internship"))
            except ValueError:
                work_type = WorkType.INTERNSHIP

            job = Job(
                id=row.get("id", ""),
                title=row.get("title", ""),
                company=row.get("company", ""),
                description=row.get("description", ""),
                required_skills=req_skills,
                preferred_skills=pref_skills,
                location=row.get("location", ""),
                location_type=location_type,
                work_type=work_type,
                experience_level=row.get("experience_level", "Student"),
                stipend_salary=row.get("stipend_salary"),
                posted_date=row.get("posted_date"),
                application_url=row.get("application_url"),
                company_url=row.get("company_url"),
                source=row.get("source", "CSV Dataset"),
                is_suspicious_flag=row.get("is_suspicious_flag", "").strip().lower() == "true",
                suspicious_reasons=suspicious_reasons
            )
            jobs.append(job)

    return jobs
