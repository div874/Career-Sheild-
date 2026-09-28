import os
import uuid
from pathlib import Path
from fastapi import APIRouter, File, UploadFile, HTTPException, status
from app.resume.parser import extract_text_from_pdf

router = APIRouter(prefix="/api/v1/resume", tags=["Resume"])

UPLOAD_DIR = Path("data/uploads")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)


@router.post("/upload")
async def upload_resume(file: UploadFile = File(...)):
    """
    Upload a PDF resume, save it securely, and extract raw text.
    """
    if not file.filename or not file.filename.lower().endswith(".pdf"):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid file format. Only PDF files (.pdf) are supported."
        )

    # Generate unique filename to avoid overwrites or path traversal
    file_extension = Path(file.filename).suffix
    unique_filename = f"{uuid.uuid4().hex}{file_extension}"
    file_path = UPLOAD_DIR / unique_filename

    try:
        contents = await file.read()
        if len(contents) == 0:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Uploaded PDF file is empty."
            )

        with open(file_path, "wb") as f:
            f.write(contents)

        # Extract raw text from the saved PDF
        extracted_text = extract_text_from_pdf(file_path)

        return {
            "success": True,
            "filename": file.filename,
            "stored_filename": unique_filename,
            "file_size_bytes": len(contents),
            "extracted_text": extracted_text,
            "character_count": len(extracted_text),
            "word_count": len(extracted_text.split())
        }
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to extract text from PDF: {str(e)}"
        )
    finally:
        # Safely remove uploaded PDF file after processing completes
        if file_path.exists():
            try:
                os.remove(file_path)
            except Exception:
                pass

