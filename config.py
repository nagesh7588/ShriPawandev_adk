# Configuration constants
SETTINGS = {
    "PUBLIC_DATASET": "bigquery-public-data.faa.incidents",
    "QUERY_LIMIT": 1000,
    "MIN_YEAR": "2010-01-01",
    "REQUIRED_COLS": [
        "timestamp",
        "latitude",
        "longitude",
        "airport_code",
        "aircraft_model",
        "total_fatal_injuries",
        "total_serious_injuries"
    ]
}