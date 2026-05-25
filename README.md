# Fishing Recommendation Dashboard
- A Streamlit dashboard that combines live weather data, barometric pressure trends, and Georgia DNR trout stocking reports to recommend the best fishing spots and times in North Georgia. An AI fishing guide powered by Gemini LLM explains conditions in plain English.

**Live app:** [https://fishing-ga.streamlit.app/](https://fishing-ga.streamlit.app/)

## Screenshot of App

## How it works
1. **Data ingestion** — Live hourly weather data is fetched from the Open-Meteo API for each fishing location. The Georgia DNR weekly trout stocking report is automatically parsed from a government PDF using pdfplumber.
2. **Scoring** — Each hour is scored 0–100 based on water temperature (ideal trout range: 52–64°F), barometric pressure trend (dropping pressure = active feeding), time of day (dawn/dusk windows), and precipitation.
3. **Ranking** — All spots are ranked by their best scoring hour in the next 24 hours. Spots on recently stocked waterways receive a bonus.
4. **AI Recommendation** — Scored data is passed to the Gemini LLM which generates a plain-English fishing recommendation including suggested techniques and target species.

## Features
- Live weather data from Open Meteo API: https://open-meteo.com/
- Automated PDF parsing of Georgia DNR weekly stocking reports
- Scoring Model
- Ranker that combines weather + stocking data
- AI Recommendation via Gemini LLM API

## Tech Stack
- Python
- Streamlit
- pandas
- Open-Meteo API
- pdfplumber
- Gemini LLM (integrated LLM for recommendations via REST API)
- pytz 

## How to run locally

## Project Structure