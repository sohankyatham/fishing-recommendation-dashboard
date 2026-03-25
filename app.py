# app.py
import streamlit as st
from data.weather import fetch_weather
from data.spots import SPOTS
from analysis.scoring import score_hour
from analysis.ranker import rank_spots

st.set_page_config(page_title="Fishing Conditions Dashboard", page_icon="🐠", layout="wide")
st.title("🐠 Fishing Conditions Dashboard")

# Sidebar
st.sidebar.header("Settings")

selected_spot = st.sidebar.selectbox("Choose a spot", list(SPOTS.keys()))
st.session_state["selected_spot"] = selected_spot  # save for other pages

spot = SPOTS[selected_spot]
lat, lon = spot["lat"], spot["lon"]

time_mode = st.sidebar.radio("Recommendation horizon", ["Today", "Next 3 days"])
show_details = st.sidebar.toggle("Show details table", value=True)

# Main area
st.subheader("📍 Selected Spot")
st.info(f"{selected_spot} | {lat}, {lon}")

weather_df = fetch_weather(lat, lon)
weather_df["score"] = weather_df.apply(score_hour, axis=1)

st.subheader("🏆 Best Spots Right Now")
ranked = rank_spots()
st.dataframe(ranked)

if show_details:
    st.subheader("Raw Weather Data")
    st.dataframe(weather_df)