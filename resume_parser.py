# resume_parser.py

import fitz  # This is PyMuPDF

def extract_text_from_pdf(uploaded_file):
    text = ""
    # 'uploaded_file' is a file-like object from Streamlit uploader
    with fitz.open(stream=uploaded_file.read(), filetype="pdf") as doc:
        for page in doc:
            text += page.get_text()
    return text


