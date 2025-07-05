import os
from pathlib import Path
from dotenv import load_dotenv
from google.cloud import bigquery
from flask import Flask, jsonify

# Import your existing agents
from agents.data_collector_offline import DataCollectorAgent
from agents.data_preprocessor import DataPreprocessorAgent
from agents.ml_agent import MLAgent
from agents.visualization_agent import VisualizationAgent
from agents.report_agent import ReportAgent

# Define base paths and environment variables
BASE_DIR = Path(__file__).resolve().parent
SERVICE_ACCOUNT_PATH = BASE_DIR / "myfirstproject" / "service-account.json"
load_dotenv()

# Initialize Flask app
app = Flask(__name__)

def initialize_bigquery_client():
    """Initialize BigQuery client using service account credentials"""
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = str(SERVICE_ACCOUNT_PATH)
    return bigquery.Client.from_service_account_json(
        str(SERVICE_ACCOUNT_PATH),
        project=os.getenv("GOOGLE_PROJECT_ID")
    )

def run_agents():
    """Run the existing ML pipeline and return the result context."""
    print("🚀 Starting airplane crash prediction system...")
    print(f"Using service account at: {SERVICE_ACCOUNT_PATH}")

    context = {}

    try:
        # Step 1: BigQuery client
        client = initialize_bigquery_client()

        # Step 2: Collect Data
        print("\n📥 Running DataCollectorAgent...")
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

        print("\n✅ All agents completed successfully!")
        return context

    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
        return {"error": str(e)}

# Flask routes
@app.route("/", methods=["GET"])
def index():
    return "Hello, Cloud Run! ✅ The service is up."

@app.route("/run_model", methods=["GET"])
def run_model():
    context = run_agents()
    
    return jsonify({
        "status": "success",
        "report_path": context.get("report_path"),
        "visual_path": context.get("visual_path"),
        "message": "Model pipeline completed successfully"
    })



# Entrypoint for Cloud Run
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)
