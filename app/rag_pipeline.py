from app.db_handler import search_profiles
from app.llm_handler import generate_feedback

def run_search(query: str, top_k: int = 5):
    matches = search_profiles(query, top_k=top_k)
    results = []

    for profile, score in matches:
        insights, compatibility = generate_feedback(query, profile)
        results.append({
            "profile": profile,
            "insights": insights,
            "compatibility": compatibility
        })

    return results
