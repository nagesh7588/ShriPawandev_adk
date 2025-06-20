import pandas as pd

class DataPreprocessorAgent:
    def run(self, context):
        try:
            print("🔧 Preprocessing data...")
            df = context.get("raw_data")

            if df is None:
                raise ValueError("No raw data found in context")

            # Minimal preprocessing
            df = df.dropna(how="all")

            context["preprocessed_data"] = df  # ✅ must be set
            print(f"✅ Data preprocessed. Shape: {df.shape}")
            return context

        except Exception as e:
            print(f"❌ Error: {e}")
            raise e
