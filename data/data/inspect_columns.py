import pandas as pd
import os

# Get absolute path to the csv_exports folder
current_dir = os.path.dirname(os.path.abspath(__file__))
csv_dir = os.path.join(current_dir, "csv_exports")

# Read CSVs and print column names
try:
    country = pd.read_csv(os.path.join(csv_dir, "country.csv"))
    print("📄 country.csv columns:", list(country.columns))
except Exception as e:
    print("❌ country.csv error:", e)

try:
    injury = pd.read_csv(os.path.join(csv_dir, "injury.csv"))
    print("\n📄 injury.csv columns:", list(injury.columns))
except Exception as e:
    print("❌ injury.csv error:", e)

try:
    aircraft = pd.read_csv(os.path.join(csv_dir, "aircraft.csv"))
    print("\n📄 aircraft.csv columns:", list(aircraft.columns))
except Exception as e:
    print("❌ aircraft.csv error:", e)
