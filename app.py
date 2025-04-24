# app.py

import streamlit as st
from resume_parser import extract_text_from_pdf
from jd_parser import extract_text_from_jd
from skill_matcher import match_score

st.set_page_config(page_title="Resume Matcher", page_icon="📄", layout="centered")

st.title("📄 Resume Matcher AI")
st.subheader("Upload a resume and job description to see how well they match!")

# Upload Resume
resume_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])
jd_file = st.file_uploader("Upload Job Description (TXT)", type=["txt"])

if st.button("Compare") and resume_file and jd_file:
    with st.spinner("Extracting and analyzing..."):
        resume_text = extract_text_from_pdf(resume_file)
        jd_text = extract_text_from_jd(jd_file)
        result = match_score(resume_text, jd_text)

    st.success("✅ Analysis Complete!")
    st.metric("🎯 Match Score", f"{result['match_score']}%")
    st.write("✅ **Matched Keywords**:", ", ".join(result['matched_keywords']))
    st.write("📄 **Total Resume Keywords**:", result['total_resume_keywords'])
    st.write("📝 **Total JD Keywords**:", result['total_jd_keywords'])

     #After extracting resume_text and job_desc_text
score, matched, missing = match_score(resume_text, jd_text)

st.subheader("🎯 Resume Match Score")
st.progress(int(score))
st.write(f"**Score: {score}%**")

if score >= 80:
    st.success("✅ Great match! Your resume aligns well with the job.")
elif score >= 50:
    st.warning("⚠️ Decent match. Consider adding or improving the following:")
    st.write(", ".join(missing[:10]))  # Show first 10 missing keywords
else:
    st.error("❌ Low match. You may be missing key skills or keywords.")
    st.write("Suggested additions:", ", ".join(missing[:10]))



