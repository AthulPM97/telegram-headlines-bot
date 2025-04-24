import pdfplumber
import io

def extract_first_word(pdf_bytes: bytes) -> str:
    with pdfplumber.open(io.BytesIO(pdf_bytes)) as pdf:
        first_page = pdf.pages[0]
        text = first_page.extract_text()
        return text.split()[0] if text else "No text found!"