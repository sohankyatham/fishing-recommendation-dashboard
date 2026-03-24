# app.py
import streamlit as st
import pandas as pd
import altair as alt
import requests

# Get hourly weather data from Open-Meteo API & return as a DataFrame
def fetch_weather(lat, lon):
    url = "https://api.open-meteo.com/v1/forecast"

    params = {
        "latitude": lat,
        "longitude": lon,
        "hourly": "temperature_2m,precipitation,surface_pressure",
        "forecast_days": 2,
        "timezone": "America/New_York"
    }

    response = requests.get(url, params=params)

    data = response.json()

    hourly = data["hourly"]

    df = pd.DataFrame({
        "time": hourly["time"],
        "temperature_f": [(t * 9/5) + 32 for t in hourly["temperature_2m"]], # Convert Celsius to Fahrenheit
        "precipitation": hourly["precipitation"],
        "pressure": hourly["surface_pressure"]
    })
    
    return df

# Page configuration
st.set_page_config(page_title="Fishing Conditions Dashboard", page_icon="🐠", layout="wide")

# Title 
st.title("🐠 Fishing Conditions Dashboard")
st.success("North GA fishing recommendations using government data + temperature + pressure.")

# Sidebar for controls 
st.sidebar.header("Settings")

spots = {
    "Denmark HS - Use to check weather data": {"lat": 34.0909, "lon": -84.1345},
    "Lake Herrick (Athens)": {"lat": 33.9299, "lon": -83.3739},
    "Buford Dam Tailwater": {"lat": 34.1571, "lon": -84.0706},
    "Bowmans Island": {"lat": 34.1465, "lon": -84.0779},
    "Settles Bridge": {"lat": 34.1527, "lon": -84.0955},
    "McGinnis Ferry": {"lat": 34.1169, "lon": -84.1437},
    "Abbotts Bridge": {"lat": 34.0834, "lon": -84.2182},
    "Medlock Bridge": {"lat": 34.0476, "lon": -84.2277},
}

# Dropdown allowing the user to select a fishing location.
selected_spot = st.sidebar.selectbox(
    "Choose a spot",
    list(spots.keys())
)

lat = spots[selected_spot]["lat"]
lon = spots[selected_spot]["lon"]

time_mode = st.sidebar.radio("Recommendation horizon", ["Today", "Next 3 days"])
show_details = st.sidebar.toggle("Show details table", value=True)


# ===========================================================
# MAIN DASHBOARD AREA
# ===========================================================


st.subheader("Recommendation")
st.write(f"Latitude: {lat}, Longitude: {lon}")
st.info(f"Selected spot: **{selected_spot}** | Mode: **{time_mode}**")

st.success("Below is accurate weather data from Open-Meteo.")
weather_df = fetch_weather(lat, lon)
st.dataframe(weather_df)

st.subheader("Charts")
st.write("Charts will appear here.")

weather_df["time"] = pd.to_datetime(weather_df["time"])

temp_chart = (
    alt.Chart(weather_df)
    .mark_line(point=True)
    .encode(
        x=alt.X("time:T", title="Time"),
        y=alt.Y("temperature_f:Q", title="Temperature (°F)"),
        tooltip=[
            alt.Tooltip("time:T", title="Time"),
            alt.Tooltip("temperature_f:Q", title="Temp (°F)", format=".1f"),
            alt.Tooltip("precipitation:Q", title="Precipitation", format=".2f"),
            alt.Tooltip("pressure:Q", title="Pressure", format=".1f"),
        ],
    )
    .properties(
        width="container",
        height=400,
        title="Temperature Over Time"
    )
    .interactive()
)

st.altair_chart(temp_chart, use_container_width=True)

if show_details:
    st.subheader("Details")
    st.write("A table of the best hours will appear here.")