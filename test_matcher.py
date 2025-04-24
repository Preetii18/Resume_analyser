from skill_matcher import match_score

resume = "I have experience in Python, Machine Learning, and web development."
jd = "Looking for a developer with experience in Python, Django, and AI."

score, matched, missing = match_score(resume, jd)

print("Score:", score)
print("Matched Keywords:", matched)
print("Missing Keywords:", missing)
