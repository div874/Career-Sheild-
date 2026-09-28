import io
from fastapi.testclient import TestClient
import pypdf
from app.main import app

client = TestClient(app)


def test_upload_non_pdf_fails():
    response = client.post(
        "/api/v1/resume/upload",
        files={"file": ("resume.txt", b"Plain text file", "text/plain")}
    )
    assert response.status_code == 400
    assert "Only PDF files (.pdf) are supported" in response.json()["detail"]


def test_upload_empty_pdf_fails():
    response = client.post(
        "/api/v1/resume/upload",
        files={"file": ("empty.pdf", b"", "application/pdf")}
    )
    assert response.status_code == 400
    assert "Uploaded PDF file is empty" in response.json()["detail"]


def test_upload_valid_pdf():
    # Create valid minimal PDF using pypdf
    writer = pypdf.PdfWriter()
    writer.add_blank_page(width=612, height=792)
    buf = io.BytesIO()
    writer.write(buf)
    pdf_bytes = buf.getvalue()

    response = client.post(
        "/api/v1/resume/upload",
        files={"file": ("my_resume.pdf", pdf_bytes, "application/pdf")}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["success"] is True
    assert data["filename"] == "my_resume.pdf"
    assert "character_count" in data
    assert "word_count" in data
