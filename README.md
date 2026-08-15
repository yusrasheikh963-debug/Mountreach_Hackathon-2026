# Mountreach_Hackathon-2026
CareerNova AI

CareerNova AI is an AI-powered career intelligence platform that analyzes a user's resume and turns the information into actionable career insights. The application extracts skills and resume evidence, evaluates career compatibility, identifies skill gaps, generates a personalized roadmap, suggests opportunity signals, and provides an interactive career companion.

The project combines a FastAPI backend with a React + Vite frontend featuring animated 3D-style career visualization, interactive cards, career simulation, and resume analysis.

✨ Key Features

Resume Intelligence

Upload resumes in PDF, DOCX, DOC, TXT, or MD format.

Extract readable text from the uploaded resume.

Detect technical and professional skills from resume evidence.

Identify education, experience, projects, and certifications.

Generate a resume signal score.

Career Intelligence

Compare detected skills with predefined career profiles.

Recommend career paths based on matching skills.

Show career compatibility scores.

Display matching skills and missing skills.

Explain why a career path is recommended.

Skill Gap Analysis

Identify skills required for the selected career.

Generate a focused career roadmap.

Detect some transferable/hidden skill signals from resume content.

Career Simulation

Users can enter a skill and simulate how adding that skill can change career compatibility.

Example:

Current profile
       ↓
Add "Docker"
       ↓
Career Simulation
       ↓
Updated career compatibility

Career Companion

The dashboard includes a career companion where users can ask questions such as:

What should I focus on next?
What are my major skill gaps?

The response is grounded in the currently analyzed resume profile.

Interactive UI

The frontend includes:

Animated career intelligence core

Orbiting 3D-style visual elements

Animated skill nodes

Hover animations

Framer Motion transitions

Interactive career cards

Animated compatibility rings

Resume scanning animation

Career Twin visualization

Pointer-responsive background glow

Responsive mobile layout

🧠 AI / Analysis Architecture

The current project uses a resilient rule-based analysis layer for demo readiness.

The analyzer:

Normalizes resume text.

Detects skills using keyword/evidence matching.

Extracts major resume sections.

Calculates skill evidence scores.

Compares detected skills against career requirements.

Calculates career compatibility.

Identifies career gaps.

Generates a roadmap.

Generates opportunity/job signals.

Creates data consumed by the React dashboard.

The project also contains a separate CareerAIEngine service layer designed for future AI/LLM integration. It includes hidden-skill extraction, career matching, and skill-impact simulation.

Important: The current backend does not require an external LLM API key for the core demo flow.

🏗️ System Architecture

                         ┌─────────────────────┐
                         │       User          │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │  React Frontend     │
                         │  Vite + Framer      │
                         │  Motion + Lucide    │
                         └──────────┬──────────┘
                                    │
                           Resume Upload / API
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │   FastAPI Backend   │
                         │      main.py        │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │ Resume Text Parser  │
                         │ PDF / DOCX / DOC    │
                         │ TXT / MD            │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │ Career Analyzer     │
                         │ Skill Detection     │
                         │ Career Matching     │
                         │ Gap Analysis        │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │ Career Intelligence │
                         │ Profile / Roadmap   │
                         │ Jobs / Simulation   │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │ CareerNova         │
                         │ Dashboard           │
                         └─────────────────────┘

📁 Project Structure

CareerNova-AI/
│
├── backend/
│   ├── main.py
│   ├── schemas.py
│   ├── requirements.txt
│   │
│   └── services/
│       ├── analyzer.py
│       └── ...
│
├── frontend/
│   ├── main.jsx
│   ├── analyzer.js
│   ├── style.css
│   ├── package.json
│   └── ...
│
├── README.md
└── .gitignore

If the project currently keeps the frontend and backend files in a single directory, the structure can be adjusted accordingly. The important separation is between the React client and FastAPI server.

⚙️ Backend Setup

1. Create a Python Virtual Environment

From the backend/project directory:

python -m venv .venv

Windows

.venv\Scripts\activate

macOS / Linux

source .venv/bin/activate

2. Install Backend Dependencies

pip install -r requirements.txt

The backend uses packages including:

FastAPI

Uvicorn

python-multipart

PyPDF

python-docx

3. Start the FastAPI Server

If main.py is inside the backend package:

uvicorn backend.main:app --reload

If you are already inside the backend directory:

uvicorn main:app --reload

The backend will normally run at:

http://127.0.0.1:8000

💻 Frontend Setup

The frontend uses React + Vite.

1. Install Node.js

Make sure Node.js and npm are installed.

Check:

node --version
npm --version

2. Install Frontend Packages

Navigate to the frontend directory:

cd frontend

Then:

npm install

The project uses:

React

React DOM

Vite

Framer Motion

Lucide React

React Router DOM

Recharts

Mammoth

PDF.js

3. Start the Frontend

npm run dev

Vite will display the local development URL, normally:

http://localhost:5173

🔌 Backend API

The frontend communicates with:

http://localhost:8000/api

Health Check

GET /health

Response:

{
  "status": "ok"
}

Resume Upload

POST /api/resume/upload

Uploads and analyzes a resume.

Supported formats:

PDF
DOCX
DOC
TXT
MD

The frontend sends the resume using FormData.

Profile

GET /api/profile

Returns the current analyzed profile.

Career Recommendations

GET /api/careers

Returns career recommendations.

Skill Gap

GET /api/skills/gap

Returns the selected career and identified skill gaps.

Example:

{
  "career": "AI / ML Engineer",
  "gaps": [
    "Docker",
    "Machine Learning"
  ]
}

Job / Opportunity Signals

GET /api/jobs

Returns opportunity signals generated from career matches.

Career Twin

GET /api/career-twin

Returns the complete current career intelligence profile.

Career Simulation

POST /api/career/simulate

Request:

{
  "skill": "Docker"
}

The endpoint recalculates career scores based on the simulated skill.

Career Companion

POST /api/companion/chat

Request:

{
  "message": "What should I focus on next?"
}

Response:

{
  "reply": "..."
}

📄 Resume Processing

The backend uses different processing methods depending on the uploaded file.

PDF

Text is extracted using pypdf.

DOCX

Text is extracted using python-docx.

TXT / MD

The content is decoded as UTF-8.

DOC

Legacy .doc files require the Antiword command-line utility.

If Antiword is unavailable, the backend returns an error recommending PDF, DOCX, or TXT instead.

🎨 Frontend Experience

The landing page is designed as an immersive AI career-intelligence experience.

Main Sections

Landing Page
    │
    ├── Navigation
    ├── AI Career Intelligence Hero
    ├── Career Core Visualization
    ├── Resume → AI Understanding → Career Intelligence
    ├── AI Resume Intelligence
    ├── Career Intelligence Graph
    └── Future / Upload CTA

After resume analysis, the application switches to the dashboard:

Career Command Center
    │
    ├── Career Readiness
    ├── Resume Signal
    ├── Opportunity Horizon
    ├── Skill Constellation
    ├── AI Career Roadmap
    ├── What-If Skill Simulator
    ├── Opportunity Signals
    └── Career Companion

🌌 Career Twin Visualization

The Core component creates the main visual identity of CareerNova.

It contains:

Central AI nucleus

Multiple orbit rings

Career-related nodes

Floating labels

Animated rotation

Pulsing/breathing center

Small and large visualization modes

The frontend also tracks pointer movement and updates CSS variables to create a subtle mouse-responsive background glow.

📊 Career Scoring

Career compatibility is calculated from the skills detected in the resume.

For each career:

Required Skills
       ↓
Detected Skills
       ↓
Matching Skills
       +
Missing Skills
       ↓
Compatibility Score

The analyzer currently contains career profiles such as:

AI / ML Engineer

Data Analyst

Frontend Engineer

Backend Engineer

Cloud Engineer

Product Designer

Cybersecurity Analyst

Product Manager

Software Engineer

Business Development Associate

🧩 Detected Skill Categories

The analyzer currently checks for skills including:

Python

JavaScript

Java

SQL

AWS

Docker

Kubernetes

Git

Machine Learning

Data Analysis

Excel

Figma

UI/UX Design

Project Management

Communication

C++

C

HTML/CSS

REST APIs

Cybersecurity

Linux

Sales

The detected skills are converted into evidence-based scores for the dashboard.

🗺️ Personalized Roadmap

The roadmap is generated from missing skills for the highest-ranked career path.

Example:

Phase 1
   ↓
Build Docker Skills

Phase 2
   ↓
Build Machine Learning Skills

Phase 3
   ↓
Build Portfolio Project

Phase 4
   ↓
Strengthen Career Readiness

The exact roadmap changes according to the analyzed resume.

🔄 Application Flow

1. User opens CareerNova
             ↓
2. Upload Resume
             ↓
3. FastAPI receives file
             ↓
4. Resume text is extracted
             ↓
5. Analyzer detects evidence
             ↓
6. Skills are identified
             ↓
7. Career paths are scored
             ↓
8. Skill gaps are calculated
             ↓
9. Roadmap and opportunities are generated
             ↓
10. React Dashboard displays results
             ↓
11. User can simulate skills
             ↓
12. User can interact with Career Companion

🧪 Testing

Backend

Open:

http://127.0.0.1:8000/docs

FastAPI provides interactive Swagger documentation.

Test:

GET /health

Then:

POST /api/resume/upload

Upload a text-based resume and inspect the returned JSON.

Frontend

Open the Vite URL:

http://localhost:5173

Test:

Landing page

Resume upload

Analysis loading screen

Career dashboard

Career compatibility cards

Skill constellation

Roadmap

Skill simulation

Career Companion

⚠️ Current Limitations

The current implementation is optimized for a reliable project/demo experience.

In-memory profile

The backend stores the active analysis in:

current = {}

Therefore, the analyzed profile is temporary and can be lost when the server restarts.

Rule-based skill detection

The main analyzer currently uses predefined keywords and evidence matching rather than a full LLM-based semantic understanding system.

Job data

The current /api/jobs response represents curated role signals generated from career matches. It is not a live job-board integration.

DOC support

Legacy .doc processing depends on Antiword being installed on the system.

🔮 Future Scope

CareerNova can be expanded with:

LLM-powered resume understanding

Real ATS scoring

Resume improvement recommendations

Personalized learning resources

Real-time job APIs

LinkedIn profile analysis

GitHub profile analysis

Skill verification

User authentication

PostgreSQL/MongoDB persistence

Multiple user profiles

Resume version comparison

AI-generated interview questions

AI interview evaluation

Voice-based career companion

Real-time labor-market trends

Advanced Career Twin graph

Personalized course recommendations

🔐 Security Recommendations for Production

Before deploying publicly:

Add authentication and authorization.

Validate uploaded file size and MIME type.

Store uploaded resumes securely.

Avoid keeping user profiles in global memory.

Add database persistence.

Configure production CORS origins instead of broad development settings.

Never commit API keys or secrets.

Add rate limiting.

Sanitize and validate user input.

Use HTTPS in production.

📦 Available Scripts

Frontend

npm run dev

Starts the Vite development server.

npm run build

Creates a production frontend build.

npm run preview

Previews the production build locally.

🏆 Project Highlights

CareerNova AI combines:

Resume Analysis + Career Matching + Skill Gap Detection + Career Roadmap + Skill Simulation + Career Companion + Interactive Career Twin

into a single career intelligence platform.

Instead of treating a resume as a static document, CareerNova transforms it into a dynamic profile that helps users understand:

What I know
     ↓
What I am good at
     ↓
Where I fit
     ↓
What I am missing
     ↓
What I should learn
     ↓
Where I can go next

📌 Project Name

CareerNova AI — AI-Powered Career Intelligence & Career Companion

Tagline

Your Career. Understood by AI.

📜 License

This project is intended for educational, demonstration, and hackathon/project purposes.
