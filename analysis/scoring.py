def score_hour(row):
    score = 0

    # Temperature (35 points max)
    if 50 <= row["temperature_f"] <= 65:
        score += 35
    elif 45 <= row["temperature_f"] <= 70:
        score += 15
    # else: temperature is not ideal, dont add any points

    # Pressure trend (30 points max)
    # Fish are more active when the pressure is rising because fish feed more
    # So pressure_change should be positive which means it's rising
    if row["pressure_change"] > 0.5:
        score += 30
    elif row["pressure_change"] > 0:
        score += 15
    elif row["pressure_change"] < -1:
        score -= 10  # actively falling pressure, fish are less active 

    # Time of day (20 points max) - dawn and dusk are the best times to fish
    hour = row["time"].hour  # extract the hour number (0-23) from datetime
    
    # dawn or dusk
    if 5 <= hour <= 9 or 17 <= hour <= 20:
        score += 20  
    # midday - not best conditions
    elif 10 <= hour <= 16:
        score += 5   

    # Precipitation (15 points max)
    if row["precipitation"] == 0:
        score += 10  # dry is fine
    elif row["precipitation"] <= 2:
        score += 15  # light rain is actually best
    elif row["precipitation"] > 5:
        score -= 10  # heavy rain muddies water

    # Stocking bonus - need to implement this later when we have the data
    # if row["was_stocked"]:
    #     score += 20

    # never return negative
    return max(0, score)  