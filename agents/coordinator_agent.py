from agents.data_collector import DataCollectorAgent
from agents.preprocessing_agent import PreprocessingAgent
from agents.ml_agent import MLAgent
from agents.report_agent import ReportAgent

class CoordinatorAgent:
    def run(self):
        context = {}

        print("🛰️ Running DataCollectorAgent...")
        context = DataCollectorAgent().run(context)

        print("🧹 Running PreprocessingAgent...")
        context = PreprocessingAgent().run(context)

        print("🤖 Running MLAgent...")
        context = MLAgent().run(context)

        print("📊 Running ReportAgent...")
        context = ReportAgent().run(context)
