import pandas as pd
import os

# Define the path
current_dir = os.path.dirname(os.path.abspath(__file__))
csv_dir = os.path.join(current_dir, "csv_exports")

# Read CSVs
injury_df = pd.read_csv(os.path.join(csv_dir, "injury.csv"), low_memory=False)
aircraft_df = pd.read_csv(os.path.join(csv_dir, "aircraft.csv"), low_memory=False)
country_df = pd.read_csv(os.path.join(csv_dir, "country.csv"))

# ✅ Merge injury and aircraft on ev_id and Aircraft_Key
merged_df = pd.merge(injury_df, aircraft_df, on=["ev_id", "Aircraft_Key"], how="inner")

# 🔄 Optional: merge with country.csv using owner_country
final_df = pd.merge(merged_df, country_df, left_on="owner_country", right_on="COUNTRY_CODE", how="left")

# Save result
output_path = os.path.join(csv_dir, "merged_output.csv")
final_df.to_csv(output_path, index=False)

print(f"✅ Merged file saved to: {output_path}")
print("🧾 Final shape:", final_df.shape)
