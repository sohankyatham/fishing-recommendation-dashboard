# app.py
import streamlit as st
from data.weather import fetch_weather
from data.spots import SPOTS
from analysis.scoring import score_hour
from analysis.ranker import rank_spots
from data.stocking import fetch_stocking_data

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

ranked = rank_spots()

# Top recommendation card
best = ranked.iloc[0]  # first row = highest scored spot

st.subheader("🎣 Best Spot Right Now")
st.success(f"""
**{best['spot']}**  
Best time to go: {best['best_time']}  
Conditions score: {best['best_score']}/100  
Water temp: {best['temp_f']}°F  
Pressure trend: {'↓ Dropping (fish feeding)' if best['pressure_change'] < 0 else '↑ Rising (fish lethargic)'}
""")

# Full ranked table below
st.subheader("🏆 All Spots Ranked")
st.dataframe(ranked, use_container_width=True)

stocking_df = fetch_stocking_data()
st.subheader("🐟 This Week's Stocking Report")
st.dataframe(stocking_df)

if show_details:
    st.subheader("Raw Weather Data")
    st.dataframe(weather_df)