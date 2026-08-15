import re

SKILLS = {
    "Python": ["python", "pandas", "numpy", "django", "flask", "fastapi"], "JavaScript": ["javascript", "typescript", "react", "node.js", "nodejs", "next.js"],
    "Java": ["java", "spring boot", "spring"], "SQL": ["sql", "postgresql", "mysql", "sqlite"], "AWS": ["aws", "amazon web services", "ec2", "s3", "lambda"],
    "Docker": ["docker", "containerization", "containers"], "Kubernetes": ["kubernetes", "k8s"], "Git": ["git", "github", "gitlab"],
    "Machine Learning": ["machine learning", "deep learning", "scikit-learn", "tensorflow", "pytorch"], "Data Analysis": ["data analysis", "tableau", "power bi", "analytics"],
    "Excel": ["excel", "spreadsheets"], "Figma": ["figma", "wireframe", "prototyping"], "UI/UX Design": ["user experience", "user interface", "ux design", "ui design"],
    "Project Management": ["project management", "agile", "scrum", "jira"], "Communication": ["communication", "stakeholder", "presentation"],
    "C++": ["c++"], "C": ["c programming", " c "], "HTML/CSS": ["html", "css", "tailwind"], "REST APIs": ["rest api", "restful", "api development"],
    "Cybersecurity": ["cybersecurity", "security", "penetration testing"], "Linux": ["linux", "unix"], "Sales": ["sales", "crm", "lead generation"],
}
CAREERS = {
 "AI / ML Engineer": ["Python", "Machine Learning", "SQL", "Docker", "Git"], "Data Analyst": ["SQL", "Data Analysis", "Excel", "Python", "Communication"],
 "Frontend Engineer": ["JavaScript", "HTML/CSS", "Git", "REST APIs", "Figma"], "Backend Engineer": ["Python", "Java", "SQL", "REST APIs", "Docker"],
 "Cloud Engineer": ["AWS", "Docker", "Kubernetes", "Linux", "Git"], "Product Designer": ["Figma", "UI/UX Design", "Communication", "Project Management"],
 "Cybersecurity Analyst": ["Cybersecurity", "Linux", "Python", "Git", "REST APIs"], "Product Manager": ["Project Management", "Communication", "Data Analysis", "Figma", "SQL"],
 "Software Engineer": ["Python", "JavaScript", "Java", "Git", "SQL"], "Business Development Associate": ["Sales", "Communication", "Data Analysis", "Project Management"]
}

def section(text, names):
    pattern = r"(?:^|\n)\s*(?:" + "|".join(names) + r")\s*[:\n](.*?)(?=\n\s*(?:education|experience|projects?|skills?|certifications?|achievements?|summary|objective|languages?)\s*[:\n]|\Z)"
    found = re.search(pattern, text, re.I | re.S)
    return found.group(1).strip() if found else ""

def evidence_count(text, terms):
    return sum(len(re.findall(r"(?<!\w)" + re.escape(t) + r"(?!\w)", text, re.I)) for t in terms)

def extract_name(text):
    for line in text.splitlines()[:7]:
        clean = re.sub(r"[^A-Za-z .'-]", "", line).strip()
        if 3 <= len(clean) <= 55 and 1 < len(clean.split()) <= 5 and not re.search(r"resume|curriculum|engineer|developer|analyst|email|phone", clean, re.I): return clean.title()
    return "Candidate"

def analyze(text, filename="resume"):
    clean = re.sub(r"\s+", " ", text).strip()
    lower = " " + clean.lower() + " "
    counts = {s: evidence_count(lower, terms) for s, terms in SKILLS.items()}
    detected = [s for s, c in counts.items() if c]
    skills = [{"name": s, "evidence": counts[s], "level": "Strong evidence" if counts[s] >= 3 else "Evidence found", "score": min(92, 42 + counts[s] * 13 + (10 if re.search(r"experience|intern|worked|developed", lower) else 0))} for s in detected]
    skills.sort(key=lambda x: x["score"], reverse=True)
    projects = section(text, ["projects?", "personal projects?"])
    experience = section(text, ["experience", "work experience", "employment", "internships?"])
    education = section(text, ["education", "academic background"])
    certs = section(text, ["certifications?", "licenses?"])
    matches=[]
    for career, req in CAREERS.items():
        owned=[x for x in req if x in detected]; missing=[x for x in req if x not in detected]
        score=round(20 + (len(owned)/len(req))*68 + min(12, len(projects.split())/35 + len(experience.split())/45))
        if owned: matches.append({"name":career,"score":min(97,score),"matchingSkills":owned,"gaps":missing,"why":"Evidence found for " + ", ".join(owned[:3]) + "."})
    matches.sort(key=lambda x:x["score"], reverse=True)
    top=matches[0] if matches else {"name":"Explore your strengths","score":0,"matchingSkills":[],"gaps":[],"why":"Add clearer skills, projects, or experience to unlock tailored paths."}
    implied={"REST APIs": ["api", "backend", "endpoint"], "Project Management": ["led", "coordinated", "managed"], "Communication": ["presented", "stakeholder", "collaborated"], "Git": ["github", "version control"], "Data Analysis": ["dashboard", "visualization", "insights"]}
    hidden=[skill for skill, terms in implied.items() if skill not in detected and any(t in lower for t in terms)]
    total = len(clean.split()); content_score = min(30, total/18); structure = sum(bool(x) for x in [education,experience,projects,certs,section(text,["skills?"])]) * 8
    resume_score = round(min(96, 20+content_score+structure+min(16,len(detected)*2)))
    readiness=round(min(95, (top["score"]*.62) + (12 if experience else 0) + (10 if projects else 0) + (8 if education else 0)))
    roadmap=[{"phase":f"Phase {i+1}","title":f"Build {gap}","detail":f"Learn {gap} through a focused mini-project aligned with {top['name']}."} for i,gap in enumerate(top["gaps"][:4])]
    if not roadmap: roadmap=[{"phase":"Next step","title":"Deepen your portfolio","detail":f"Turn your {top['matchingSkills'][0] if top['matchingSkills'] else 'core'} evidence into a measurable case study."}]
    jobs=[{"title":m["name"],"company":"Curated role match","match":m["score"],"matchingSkills":m["matchingSkills"],"missingSkills":m["gaps"][:3],"explanation":m["why"]} for m in matches[:4]]
    return {"candidate":{"name":extract_name(text),"filename":filename},"overview":{"resumeScore":resume_score,"careerReadiness":readiness,"wordCount":total},"skills":skills,"careers":matches[:5],"topCareer":top,"hiddenSkills":hidden,"gaps":top["gaps"],"roadmap":roadmap,"jobs":jobs,"sections":{"education":education,"experience":experience,"projects":projects,"certifications":certs},"source":"resume"}
