# Notes
## TRACK THESE:
- Trout stocking dates
- Weather
- Barometric Pressure 
- Water temperature
- River flow
- Moon phase

- Falling pressure is generally better for fishing



## What I learned
- Geocoding - converting a place name or address into lat/lon coordinates.



fishing-app/
│
├── app.py                  ← Landing page / main recommendation
│
├── pages/
│   ├── 1_📊_Analysis.py    ← All the charts (temp, pressure, precipitation)
│   ├── 2_🗺️_Spot_Ranker.py ← Compare all spots side by side
│   └── 3_📋_Stocking.py    ← This week's DNR stocking report table
│
├── data/
│   ├── weather.py          ← fetch_weather()
│   ├── stocking.py         ← fetch_stocking_data()
│   └── spots.py            ← spots dict + geocoding logic
│
└── analysis/
    └── scoring.py          ← score_conditions(), score_hour()