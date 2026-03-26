import pandas as pd
from datetime import datetime, timedelta
import pytz
from data.weather import fetch_weather
from data.spots import SPOTS
from analysis.scoring import score_hour
from data.stocking import fetch_stocking_data, build_stocked_name_set, get_stocking_bonus_for_spot

# Get weather for every sport, score each hour, return a ranked DataFrame of best conditions in next 24 hours
def rank_spots():
    now = datetime.now(pytz.timezone("America/New_York"))
    results = []

    # Build stocked name set once to use for all spots
    stocking_df = fetch_stocking_data()
    stocked_name_set = build_stocked_name_set(stocking_df)

    for spot_name, spot_data in SPOTS.items():
        # Fetch weather for this spot
        df = fetch_weather(spot_data["lat"], spot_data["lon"])

        # Make time column timezone-aware so we can compare to now
        df["time"] = df["time"].dt.tz_localize("America/New_York")

        # Score every hour
        df["score"] = df.apply(score_hour, axis=1)

        # Filter to future hours within next 24
        future = df[
            (df["time"] > now) &
            (df["time"] < now + timedelta(hours=24))
        ]

        # Skip if no future hours found
        if future.empty:
            continue

        # Find the best hour
        best_row = future.loc[future["score"].idxmax()]

        # Get stocking bonus for this spot
        stocking_info = get_stocking_bonus_for_spot(spot_data, stocked_name_set)
        final_score = best_row["score"] + stocking_info["stocking_bonus"]  # add bonus to score

        # Save the result
        results.append({
            "spot": spot_name,
            "best_score": final_score,
            "weather_score": best_row["score"],
            "stocking_bonus": stocking_info["stocking_bonus"],
            "stocking_status": stocking_info["stocking_status"],
            "stocking_match": stocking_info["stocking_match"],
            "best_time": best_row["time"].strftime("%a %b %d, %I:%M %p"),
            "temp_f": round(best_row["temperature_f"], 1),
            "pressure_change": round(best_row["pressure_change"], 2),
        })

    # Convert list of dicts into a DataFrame and sort by best score
    results_df = pd.DataFrame(results)
    results_df = results_df.sort_values("best_score", ascending=False)
    results_df = results_df.reset_index(drop=True)

    return results_df