"""
Resume PDF parser module using pypdf / pdfplumber.
"""
from pathlib import Path
from typing import Union
import pypdf


def extract_text_from_pdf(pdf_path: Union[str, Path]) -> str:
    """
    Extracts raw text content from a given PDF file.
    
    1. Problem: PDF files contain binary stream layouts, not plain text.
    2. Simple solution: Use pypdf to extract page text line by line.
    3. Limitation: Complex multi-column layouts or image PDFs need fallback/OCR or pdfplumber.
    """
    path = Path(pdf_path)
    if not path.exists():
        raise FileNotFoundError(f"PDF file not found at: {pdf_path}")
    
    text_content = []
    with open(path, "rb") as f:
        reader = pypdf.PdfReader(f)
        for page_idx, page in enumerate(reader.pages):
            extracted = page.extract_text()
            if extracted:
                text_content.append(extracted)
                
    return "\n\n".join(text_content)
