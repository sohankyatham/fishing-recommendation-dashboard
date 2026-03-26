import streamlit as st
import requests
import pdfplumber
import pandas as pd
import io
import re

@st.cache_data(ttl=86400)  # cache for 1 day - no point to refetch since the PDF updates once a week
# Fetch the weekly trout stocking report from Georgia DNR.
def fetch_stocking_data():
    url = "https://georgiawildlife.com/sites/default/files/wrd/pdf/trout/Weekly_Stocking_Report.pdf"

    response = requests.get(url)

    # io.BytesIO wraps the raw bytes so pdfplumber can read it
    # without saving the file to disk first
    pdf_file = io.BytesIO(response.content)

    rows = []

    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            lines = text.split("\n")

            for line in lines:
                # Each data row starts with a date like "3/16/2026"
                # Skip header lines that don't start with a date
                parts = line.strip().split()
                if len(parts) >= 3 and "/" in parts[0]:
                    date = parts[0]
                    county = parts[1]
                    # Waterbody might be multiple words so join the rest
                    waterbody = " ".join(parts[2:])
                    rows.append({
                        "date": date,
                        "county": county,
                        "waterbody": waterbody
                    })

    df = pd.DataFrame(rows)
    df["date"] = pd.to_datetime(df["date"])
    return df


# Normalize names from Georgia DNR Report to improve matching
def normalize_name(name):
    if not name:
        return ""

    name = name.lower().strip()
    name = re.sub(r"[^\w\s]", "", name)   # remove punctuation
    name = re.sub(r"\s+", " ", name)      # collapse extra spaces
    return name


# Build a set of stocked waterbody names for fast lookup when scoring spots.
def build_stocked_name_set(stocking_df):
    stocked_names = set()

    for name in stocking_df["waterbody"].dropna():
        stocked_names.add(normalize_name(name))

    return stocked_names