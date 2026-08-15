import re
from typing import List, Dict

class CareerAIEngine:
    """
    Hackathon AI Service Layer.
    Includes fallback heuristics & mock NLP for instant demo readiness,
    architected to easily drop in an LLM API key (e.g., OpenAI/Gemini/Anthropic).
    """

    def extract_hidden_skills(self, text: str) -> List[str]:
        # Simple NLP pattern matching for demo resilience
        text_lower = text.lower()
        hidden = []
        if "sentiment analysis" in text_lower or "nlp" in text_lower:
            hidden.extend(["Data Preprocessing", "Model Evaluation", "TF-IDF / Embeddings"])
        if "dashboard" in text_lower or "chart" in text_lower:
            hidden.extend(["Data Visualization", "UI/UX Metrics"])
        if "api" in text_lower or "rest" in text_lower:
            hidden.extend(["API Architecture", "Backend Orchestration"])
        return list(set(hidden))

    def calculate_career_match(self, user_skills: List[str], target_role: str) -> Dict:
        role_skills_db = {
            "AI/ML Engineer": ["Python", "Machine Learning", "SQL", "Deep Learning", "Docker", "PyTorch"],
            "Data Scientist": ["Python", "SQL", "Statistics", "Machine Learning", "Data Visualization"],
            "Full Stack Engineer": ["React", "Node.js", "Python", "SQL", "Git", "Docker"]
        }
        
        required = role_skills_db.get(target_role, ["Python", "Git"])
        matched = [s for s in user_skills if s in required]
        missing = [s for s in required if s not in user_skills]
        
        score = int((len(matched) / len(required)) * 100) if required else 50
        
        return {
            "role": target_role,
            "match_percentage": score,
            "matched_skills": matched,
            "missing_skills": missing
        }

    def simulate_skill_impact(self, current: List[str], to_learn: List[str]) -> Dict:
        combined = list(set(current + to_learn))
        roles = ["AI/ML Engineer", "Data Scientist", "Full Stack Engineer"]
        
        before = {role: self.calculate_career_match(current, role)["match_percentage"] for role in roles}
        after = {role: self.calculate_career_match(combined, role)["match_percentage"] for role in roles}
        
        return {
            "before": before,
            "after": after,
            "boost_average": sum(after.values()) // len(after) - sum(before.values()) // len(before)
        }

ai_engine = CareerAIEngine()