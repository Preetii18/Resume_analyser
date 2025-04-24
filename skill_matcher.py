# matcher.py

import re
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS

def clean_and_tokenize(text):
    text = re.sub(r'[^a-zA-Z]', ' ', text).lower()
    tokens = text.split()
    filtered_tokens = set([word for word in tokens if word not in ENGLISH_STOP_WORDS])
    return filtered_tokens

def match_score(resume_text, jd_text):
    resume_tokens = clean_and_tokenize(resume_text)
    jd_tokens = clean_and_tokenize(jd_text)

    matched_keywords = resume_tokens.intersection(jd_tokens)
    score = (len(matched_keywords) / len(jd_tokens)) * 100 if jd_tokens else 0

    return {
        "matched_keywords": list(matched_keywords),
        "match_score": round(score, 2),
        "total_resume_keywords": len(resume_tokens),
        "total_jd_keywords": len(jd_tokens),
    }





