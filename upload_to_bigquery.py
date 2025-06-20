import os
from google.cloud import bigquery
from dotenv import load_dotenv

# Load your .env if using
load_dotenv()

# Configuration
CSV_DIR = "data"
DATASET_NAME = "ntsb_aircrash_data"  # You can change it
PROJECT_ID = os.getenv("GOOGLE_PROJECT_ID") or "myfirstproject"

# Authenticate using your service account
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = os.path.join("myfirstproject", "service-account.json")

def upload_csv_to_bigquery(csv_path, table_name, dataset_id):
    client = bigquery.Client(project=PROJECT_ID)

    table_id = f"{PROJECT_ID}.{dataset_id}.{table_name}"
    job_config = bigquery.LoadJobConfig(
        source_format=bigquery.SourceFormat.CSV,
        skip_leading_rows=1,
        autodetect=True,
    )

    with open(csv_path, "rb") as source_file:
        job = client.load_table_from_file(source_file, table_id, job_config=job_config)
        job.result()

    print(f"✅ Uploaded: {table_id}")

def main():
    client = bigquery.Client(project=PROJECT_ID)

    # Create dataset if it doesn't exist
    dataset_ref = client.dataset(DATASET_NAME)
    try:
        client.get_dataset(dataset_ref)
        print(f"✅ Dataset '{DATASET_NAME}' already exists.")
    except:
        dataset = bigquery.Dataset(dataset_ref)
        dataset.location = "US"
        client.create_dataset(dataset)
        print(f"📦 Created dataset: {DATASET_NAME}")

    # Loop through CSV files and upload
    for filename in os.listdir(CSV_DIR):
        if filename.endswith(".csv"):
            table_name = os.path.splitext(filename)[0]
            upload_csv_to_bigquery(os.path.join(CSV_DIR, filename), table_name, DATASET_NAME)

    print("🎉 All files uploaded to BigQuery.")

if __name__ == "__main__":
    main()
