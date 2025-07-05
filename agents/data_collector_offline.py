# agents/data_collector_offline.py
import pandas as pd
from pathlib import Path

class DataCollectorAgent:
    def __init__(self):
        self.csv_path = Path("data/data/csv_exports/merged_output.csv")

    def run(self, context):
        try:
            print(f"📁 Loading data from: {self.csv_path}")
            df = pd.read_csv(self.csv_path)
            print(f"✅ Loaded {len(df)} rows.")
            context["raw_data"] = df  # ✅ Save data to context
            return context
        except Exception as e:
            print(f"❌ Error loading data: {e}")
            raise e
