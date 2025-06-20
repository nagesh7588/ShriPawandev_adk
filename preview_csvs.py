# preview_csvs.py
import pandas as pd

files = ['data/country.csv', 'data/injury.csv', 'data/aircraft.csv']

for file in files:
    try:
        df = pd.read_csv(file)
        print(f"\n📄 {file}")
        print(df.head(3))  # show first 3 rows
        print(f"🔢 Columns: {df.columns.tolist()}")
    except Exception as e:
        print(f"❌ Failed to read {file}: {e}")

