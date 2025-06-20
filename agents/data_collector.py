from google.cloud import bigquery
import os
from pathlib import Path
from dotenv import load_dotenv

class DataCollectorAgent:
    def __init__(self, client):
        self.client = client  # ✅ Store the BigQuery client passed from main.py

    def run(self, context):
        try:
            print("📥 Querying NTSB Accident table from BigQuery...")

            query = """
                SELECT
                    event_date,
                    investigation_type,
                    accident_number,
                    location,
                    country,
                    injury_severity,
                    aircraft_damage,
                    aircraft_category,
                    amateur_built,
                    number_of_engines,
                    engine_type,
                    purpose_of_flight,
                    total_fatal_injuries,
                    total_serious_injuries,
                    total_minor_injuries,
                    total_uninjured,
                    weather_condition,
                    broad_phase_of_flight,
                    report_status
                FROM `myfirstproject.ntsb_aircrash_data.Accident`
                WHERE event_date IS NOT NULL
                LIMIT 1000
            """

            df = self.client.query(query).to_dataframe()
            print(f"✅ Retrieved {len(df)} accident records.")
            context["accident_df"] = df
            return context

        except Exception as e:
            print(f"❌ Failed to fetch accident data: {e}")
            raise e
