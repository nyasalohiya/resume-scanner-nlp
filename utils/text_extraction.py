import fitz  # PyMuPDF
from docx import Document
import io

def extract_text_from_file(uploaded_file):
    """Extract text from PDF, DOCX, or TXT files."""
    filename = uploaded_file.name.lower()
    
    if filename.endswith('.pdf'):
        return extract_text_from_pdf(uploaded_file)
    elif filename.endswith('.docx'):
        return extract_text_from_docx(uploaded_file)
    elif filename.endswith('.txt'):
        return extract_text_from_txt(uploaded_file)
    else:
        return ""

def extract_text_from_pdf(uploaded_file):
    """Extract text from PDF using PyMuPDF."""
    try:
        pdf_bytes = uploaded_file.read()
        pdf_document = fitz.open(stream=pdf_bytes, filetype="pdf")
        text = ""
        for page_num in range(len(pdf_document)):
            page = pdf_document[page_num]
            text += page.get_text()
        return text
    except Exception as e:
        return f"Error extracting PDF: {str(e)}"

def extract_text_from_docx(uploaded_file):
    """Extract text from DOCX using python-docx."""
    try:
        docx_bytes = uploaded_file.read()
        doc = Document(io.BytesIO(docx_bytes))
        text = ""
        for para in doc.paragraphs:
            text += para.text + "\n"
        return text
    except Exception as e:
        return f"Error extracting DOCX: {str(e)}"

def extract_text_from_txt(uploaded_file):
    """Extract text from TXT file."""
    try:
        return uploaded_file.read().decode("utf-8", errors="ignore")
    except Exception as e:
        return f"Error extracting TXT: {str(e)}"
