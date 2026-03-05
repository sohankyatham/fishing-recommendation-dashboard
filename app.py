# app.py
import streamlit as st

# Page configuration
st.set_page_config(page_title="Fishing Conditions Dashboard", page_icon="🐠", layout="wide")

# Title 
st.title("🐠 Fishing Conditions Dashboard")
st.success("North GA fishing recommendations using government data + temperature + pressure.")

# Sidebar for controls 
st.sidebar.header("Settings")

spots = {
    "Lake Lanier (Cumming)": {
        "lat": 34.2076,
        "lon": -84.0790
    },
    "Chattahoochee River (Jones Bridge)": {
        "lat": 34.0335,
        "lon": -84.1790
    },
    "Chattahoochee River (Morgan Falls)": {
        "lat": 33.9606,
        "lon": -84.4142
    }
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

st.subheader("Charts")
st.write("Charts will appear here once we add weather data.")

if show_details:
    st.subheader("Details")
    st.write("A table of the best hours will appear here.")