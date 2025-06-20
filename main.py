# main.py
import os
from pathlib import Path
from dotenv import load_dotenv
from google.cloud import bigquery
from agents.data_collector_offline import DataCollectorAgent
from agents.data_preprocessor import DataPreprocessorAgent
from agents.ml_agent import MLAgent
from agents.visualization_agent import VisualizationAgent
from agents.report_agent import ReportAgent

# Define base paths and environment variables
BASE_DIR = Path(__file__).resolve().parent
SERVICE_ACCOUNT_PATH = BASE_DIR / "myfirstproject" / "service-account.json"
load_dotenv()

def initialize_bigquery_client():
    """Initialize BigQuery client using service account credentials"""
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = str(SERVICE_ACCOUNT_PATH)
    return bigquery.Client.from_service_account_json(
        str(SERVICE_ACCOUNT_PATH),
        project=os.getenv("GOOGLE_PROJECT_ID")
    )

def main():
    print("🚀 Starting airplane crash prediction system...")
    print(f"Using service account at: {SERVICE_ACCOUNT_PATH}")

    try:
        # Step 1: Initialize BigQuery Client
        client = initialize_bigquery_client()

        # Step 2: Collect Data
        print("\n📥 Running DataCollectorAgent...")
        context = {}
        collector = DataCollectorAgent()
        context = collector.run(context)

        # Step 3: Preprocess Data
        print("\n🔧 Running DataPreprocessorAgent...")
        preprocessor = DataPreprocessorAgent()
        context = preprocessor.run(context)

        # Step 4: Train Model
        print("\n🤖 Running MLAgent...")
        ml_agent = MLAgent()
        context = ml_agent.run(context)

        # Step 5: Visualize Results
        print("\n📊 Running VisualizationAgent...")
        visualizer = VisualizationAgent()
        context = visualizer.run(context)

        # Step 6: Generate Report
        print("\n📝 Running ReportAgent...")
        reporter = ReportAgent()
        context = reporter.run(context)

        # ✅ Success
        print("\n✅ All agents completed successfully!")
        print(f"📄 Report Path: {context.get('report_path')}")
        print(f"📊 Chart Path: {context.get('visual_path')}")

    except Exception as e:
        print(f"\n❌ Error: {str(e)}")

if __name__ == "__main__":
    main()
