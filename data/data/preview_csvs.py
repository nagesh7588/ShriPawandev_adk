import pandas as pd
import os

# Absolute path to current script's folder
current_dir = os.path.dirname(os.path.abspath(__file__))
csv_folder = os.path.join(current_dir, "csv_exports")

files = ["country.csv", "injury.csv", "aircraft.csv"]

for file in files:
    file_path = os.path.join(csv_folder, file)
    try:
        df = pd.read_csv(file_path)
        print(f"✅ Preview of {file}:")
        print(df.head(3), "\n")
    except Exception as e:
        print(f"❌ Failed to read {file_path}: {e}")
