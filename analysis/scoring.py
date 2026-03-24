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

    