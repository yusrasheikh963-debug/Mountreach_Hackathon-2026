import re

SKILLS={
 "Python":["python","pandas","numpy","django","flask","fastapi"],"JavaScript":["javascript","typescript","react","node.js","nodejs","next.js"],"Java":["java","spring boot","spring"],"SQL":["sql","postgresql","mysql","sqlite"],"AWS":["aws","amazon web services","ec2","s3","lambda"],"Docker":["docker","containerization"],"Kubernetes":["kubernetes","k8s"],"Git":["git","github","gitlab"],"Machine Learning":["machine learning","deep learning","scikit-learn","tensorflow","pytorch"],"Data Analysis":["data analysis","tableau","power bi","analytics"],"Excel":["excel","spreadsheets"],"Figma":["figma","wireframe","prototyping"],"UI/UX Design":["user experience","user interface","ux design","ui design"],"Project Management":["project management","agile","scrum","jira"],"Communication":["communication","stakeholder","presentation"],"HTML/CSS":["html","css","tailwind"],"REST APIs":["rest api","restful","api development"],"Cybersecurity":["cybersecurity","penetration testing"],"Linux":["linux","unix"],"Sales":["sales","crm","lead generation"]}
CAREERS={"AI / ML Engineer":["Python","Machine Learning","SQL","Docker","Git"],"Data Analyst":["SQL","Data Analysis","Excel","Python","Communication"],"Frontend Engineer":["JavaScript","HTML/CSS","Git","REST APIs","Figma"],"Backend Engineer":["Python","Java","SQL","REST APIs","Docker"],"Cloud Engineer":["AWS","Docker","Kubernetes","Linux","Git"],"Product Designer":["Figma","UI/UX Design","Communication","Project Management"],"Cybersecurity Analyst":["Cybersecurity","Linux","Python","Git","REST APIs"],"Product Manager":["Project Management","Communication","Data Analysis","Figma","SQL"],"Software Engineer":["Python","JavaScript","Java","Git","SQL"],"Business Development Associate":["Sales","Communication","Data Analysis","Project Management"]}

def _section(text,names):
 p=r"(?:^|\n)\s*(?:"+"|".join(names)+r")\s*[:\n](.*?)(?=\n\s*(?:education|experience|projects?|skills?|certifications?|achievements?|summary|objective|languages?)\s*[:\n]|\Z)"
 m=re.search(p,text,re.I|re.S);return m.group(1).strip() if m else ""
def _count(text,terms):return sum(len(re.findall(r"(?<!\w)"+re.escape(t)+r"(?!\w)",text,re.I)) for t in terms)
def _name(text):
 for line in text.splitlines()[:7]:
  value=re.sub(r"[^A-Za-z .'-]","",line).strip()
  if 3<=len(value)<=55 and 1<len(value.split())<=5 and not re.search(r"resume|curriculum|engineer|developer|analyst|email|phone",value,re.I):return value.title()
 return "Candidate"
def analyze(text,filename="resume"):
 clean=re.sub(r"\s+"," ",text).strip();low=" "+clean.lower()+" ";counts={s:_count(low,t) for s,t in SKILLS.items()};detected=[s for s,c in counts.items() if c]
 skills=sorted([{"name":s,"evidence":counts[s],"level":"Strong evidence" if counts[s]>=3 else "Evidence found","score":min(92,42+counts[s]*13+(10 if re.search(r"experience|intern|worked|developed",low) else 0))}for s in detected],key=lambda x:x["score"],reverse=True)
 projects=_section(text,["projects?","personal projects?"]);experience=_section(text,["experience","work experience","employment","internships?"]);education=_section(text,["education","academic background"]);certs=_section(text,["certifications?","licenses?"])
 careers=[]
 for name,required in CAREERS.items():
  have=[s for s in required if s in detected];gaps=[s for s in required if s not in detected]
  if have:careers.append({"name":name,"score":min(97,round(20+len(have)/len(required)*68+min(12,len(projects.split())/35+len(experience.split())/45))),"matchingSkills":have,"gaps":gaps,"why":"Evidence found for "+", ".join(have[:3])+"."})
 careers.sort(key=lambda x:x["score"],reverse=True);top=careers[0] if careers else {"name":"Explore your strengths","score":0,"matchingSkills":[],"gaps":[],"why":"Add clearer skills, projects, or experience to unlock tailored paths."}
 implied={"REST APIs":["api","backend","endpoint"],"Project Management":["led","coordinated","managed"],"Communication":["presented","stakeholder","collaborated"],"Git":["github","version control"],"Data Analysis":["dashboard","visualization","insights"]};hidden=[s for s,t in implied.items() if s not in detected and any(x in low for x in t)]
 words=len(clean.split());score=round(min(96,20+min(30,words/18)+sum(bool(x)for x in[education,experience,projects,certs,_section(text,["skills?"])])*8+min(16,len(detected)*2)));readiness=round(min(95,top["score"]*.62+(12 if experience else 0)+(10 if projects else 0)+(8 if education else 0)))
 roadmap=[{"phase":f"Phase {i+1}","title":f"Build {gap}","detail":f"Learn {gap} through a focused mini-project aligned with {top['name']}."}for i,gap in enumerate(top["gaps"][:4])]or[{"phase":"Next step","title":"Deepen your portfolio","detail":"Turn your strongest evidence into a measurable case study."}]
 jobs=[{"title":c["name"],"company":"Curated role match","match":c["score"],"matchingSkills":c["matchingSkills"],"missingSkills":c["gaps"][:3],"explanation":c["why"]}for c in careers[:4]]
 return {"candidate":{"name":_name(text),"filename":filename},"overview":{"resumeScore":score,"careerReadiness":readiness,"wordCount":words},"skills":skills,"careers":careers[:5],"topCareer":top,"hiddenSkills":hidden,"gaps":top["gaps"],"roadmap":roadmap,"jobs":jobs,"sections":{"education":education,"experience":experience,"projects":projects,"certifications":certs},"source":"resume"}
