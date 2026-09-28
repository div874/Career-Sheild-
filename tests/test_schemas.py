from pathlib import Path
from app.config import settings
from app.resume.schemas import CandidateProfile, CareerPreferences, Education
from app.jobs.schemas import Job, WorkType, LocationType
from app.jobs.loader import load_jobs_from_csv


def test_app_config():
    assert settings.APP_NAME == "CareerShield AI"


def test_candidate_profile_schema():
    profile = CandidateProfile(
        name="Alex Student",
        email="alex@example.com",
        skills=["Python", "FastAPI", "SQL"],
        programming_languages=["Python", "JavaScript"],
        education=[
            Education(
                institution="Tech University",
                degree="B.Tech Computer Science",
                start_year=2022,
                end_year=2026
            )
        ],
        preferences=CareerPreferences(
            target_roles=["Python Backend Intern", "AI Intern"],
            preferred_locations=["Mumbai", "Remote"]
        )
    )
    assert profile.name == "Alex Student"
    assert "Python" in profile.skills
    assert profile.preferences.target_roles[0] == "Python Backend Intern"


def test_job_schema_and_loader():
    csv_path = Path(__file__).parent.parent / "data" / "sample_jobs.csv"
    assert csv_path.exists(), "sample_jobs.csv must exist in data/"

    jobs = load_jobs_from_csv(csv_path)
    assert len(jobs) >= 5
    
    first_job = jobs[0]
    assert first_job.id == "job-001"
    assert "Python" in first_job.required_skills
    assert first_job.work_type == WorkType.INTERNSHIP

    suspicious_job = [j for j in jobs if j.is_suspicious_flag][0]
    assert suspicious_job.id == "job-004"
    assert len(suspicious_job.suspicious_reasons) > 0
