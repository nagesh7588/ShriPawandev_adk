class ReportAgent:
    def __init__(self, output_path="data/report.txt"):
        self.output_path = output_path

    def run(self, context):
        print("📝 Generating report...")

        accuracy = context.get('accuracy', 'N/A')
        visual_path = context.get('visual_path', 'Not Generated')

        report = f"""
        ===== Airplane Crash Prediction Report =====

        ✅ Model Accuracy: {accuracy}
        📊 Visualization saved at: {visual_path}

        This report summarizes the prediction model results based on vehicle crash data.
        """

        with open(self.output_path, 'w') as f:
            f.write(report.strip())

        print(f"✅ Report saved to {self.output_path}")
        context['report_path'] = self.output_path
        return context
