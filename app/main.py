from pathlib import Path
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from app.config import settings
from app.resume.router import router as resume_router

app = FastAPI(
    title=settings.APP_NAME,
    version="0.1.0",
    description="CareerShield AI - Personal AI Career Intelligence Layer for Students & Job Seekers"
)

# Mount API routers
app.include_router(resume_router)

# Mount static files directory
STATIC_DIR = Path("static")
if STATIC_DIR.exists():
    app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", response_class=FileResponse)
def read_index():
    index_path = STATIC_DIR / "index.html"
    if index_path.exists():
        return FileResponse(index_path)
    return FileResponse(index_path)


@app.get("/health")
def health_check():
    return {"status": "healthy"}
