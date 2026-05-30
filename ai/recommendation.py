import streamlit as st
import os
from google import genai
from dotenv import load_dotenv

# Try Streamlit secrets first (cloud), fallback to .env for local dev
try:
    api_key = st.secrets["GEMINI_API_KEY"]
except:
    load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY")

# New google-genai client setup
client = genai.Client(api_key=api_key)

# Create a prompt based on the best spot data and get a fishing recommendation from the AI model
@st.cache_data(ttl=1800)
def generate_fishing_recommendation(best_spot_data):
    prompt = f"""
    You are an informative expert fishing guide in the state of Georgia.

    Based on the following fishing conditions, explain whether fishing will be good and give strategy advice.

    Location: {best_spot_data['spot']}
    Best time: {best_spot_data['best_time']}
    Temperature: {best_spot_data['temp_f']} F
    Pressure change: {best_spot_data['pressure_change']}
    Stocking status: {best_spot_data['stocking_status']}
    Score: {best_spot_data['best_score']}

    Explain:
    1. Why fishing conditions are good or bad
    2. What fish might be active
    3. What bait or lures to use
    4. Where in the water to fish

    Keep the response concise.
    """

    try:
        response = client.models.generate_content(
            model="gemini-3.5-flash",
            contents=prompt
        )
        return response.text
    except Exception as e:
        return "AI recommendation unavailable right now."