# Each spot has a name, coordinates, and a "pdf_name" field.
# pdf_name is how this spot appears in the DNR stocking PDF.
# If None, it means DNR doesn't stock this location.

# Spots I personally want the app to rank - DO NOT MERGE WITH STOCKING REPORT
SPOTS = {
    # Key Tailwater Fishing Locations on the Chattahoochee River:
    "Morrison Lake": {
        "lat": 34.0553,
        "lon": -84.3217,
        "stocking_names_direct": [],
        "stocking_names_related": []
    },
    "Jones Bridge Tailwater": {
        "lat": 34.0015,
        "lon": -84.2398,
        "stocking_names_direct": [],
        "stocking_names_related": ["Chattahoochee River"]
    },
    "Buford Dam Tailwater": {
        "lat": 34.1571,
        "lon": -84.0706,
        "stocking_names_direct": [],
        "stocking_names_related": ["Chattahoochee River"]
    },
    "Bowmans Island Tailwater": {
        "lat": 34.1465,
        "lon": -84.0779,
        "stocking_names_direct": [],
        "stocking_names_related": ["Chattahoochee River"]
    },
    "Settles Bridge Tailwater": {
        "lat": 34.1527,
        "lon": -84.0955,
        "stocking_names_direct": [],
        "stocking_names_related": ["Chattahoochee River"]
    },
    "McGinnis Ferry Tailwater": {
        "lat": 34.1169,
        "lon": -84.1437,
        "stocking_names_direct": [],
        "stocking_names_related": ["Chattahoochee River"]
    },
    "Abbotts Bridge Tailwater": {
        "lat": 34.0834,
        "lon": -84.2182,
        "stocking_names_direct": [],
        "stocking_names_related": ["Chattahoochee River"]
    },
    "Medlock Bridge Tailwater": {
        "lat": 34.0476,
        "lon": -84.2277,
        "stocking_names_direct": [],
        "stocking_names_related": ["Chattahoochee River"]
    },

    # Personal spots - for general fishing not trout so no stocking names
    "Mary Alice Park Beach": {
        "lat": 34.20176,
        "lon": -84.09908,
        "pdf_name": None,
    },
}