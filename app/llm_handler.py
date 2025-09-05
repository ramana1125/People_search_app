import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load .env
load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
if not GOOGLE_API_KEY:
    raise ValueError("GOOGLE_API_KEY missing in .env")

genai.configure(api_key=GOOGLE_API_KEY)

# Use a working Gemini model
MODEL_NAME = "models/gemini-2.5-pro"  # stable text generation model
model = genai.GenerativeModel(MODEL_NAME)

def generate_feedback(query, profile):
    """
    Generates compatibility insights for a profile based on the user query.
    """
    prompt = f"""
    User query: {query}

    Profile info:
    Name: {profile['name']}
    Location: {profile['location']}
    Interests: {profile['interests']}
    Bio: {profile['bio']}

    Provide:
    1. Compatibility insight (how well profile matches the query)
    2. Compatibility percentage (0-100)
    """

    response = model.generate_content(prompt)
    text = response.text.strip()

    # Parse text for compatibility percentage (simple extraction)
    import re
    match = re.search(r'Compatibility percentage[:\s]*(\d+)', text, re.IGNORECASE)
    compatibility = int(match.group(1)) if match else 50  # default 50 if not found

    return text, compatibility
