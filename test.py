from resume_parser import extract_text_from_pdf

with open(r"sample_data/sample_resume.pdf/resume_preeti.pdf", "rb") as pdf:
    resume_text = extract_text_from_pdf(pdf)
    print(resume_text)

