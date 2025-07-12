import pdfplumber
import io

def extract_text_from_pdf(uploaded_file):
    """Extract text from uploaded PDF resume."""
    text = ""
    with pdfplumber.open(io.BytesIO(uploaded_file.read())) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""
    return text.strip()