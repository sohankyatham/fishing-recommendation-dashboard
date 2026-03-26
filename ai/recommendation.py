import streamlit as st
import os
import google.generativeai as genai
from dotenv import load_dotenv


# Try Streamlit secrets first (cloud + local)
try:
    api_key = st.secrets["GEMINI_API_KEY"]
except:
    # Fallback to .env for local dev
    load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=api_key)

@st.cache_resource
def get_model():
    return genai.GenerativeModel("gemini-2.5-flash")

model = get_model()

@st.cache_resource
# Create a prompt based on the best spot data and get a fishing recommendation from the AI model
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

    # Add timeout protection and prevent infinite loading
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return "AI recommendation unavailable right now."