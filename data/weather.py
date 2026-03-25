import requests
import pandas as pd

# Fetch the hourly weather forecast from Open-Meteo API - returns pandas df with 1 row per hour
def fetch_weather(lat, lon):
    url = "https://api.open-meteo.com/v1/forecast"

    params = {
        "latitude": lat,
        "longitude": lon,
        "hourly": "temperature_2m,precipitation,surface_pressure",
        "forecast_days": 3,
        "timezone": "America/New_York"
    }

    response = requests.get(url, params=params)
    data = response.json()
    hourly = data["hourly"]

    df = pd.DataFrame({
        "time": pd.to_datetime(hourly["time"]),  # parse immediately here
        "temperature_f": [(t * 9/5) + 32 for t in hourly["temperature_2m"]],
        "precipitation": hourly["precipitation"],
        "pressure": hourly["surface_pressure"]
    })

    # Pressure change from the previous hour, diff subtracts row from previous row
    df["pressure_change"] = df["pressure"].diff()

    return df