import matplotlib.pyplot as plt
import seaborn as sns
import os

class VisualizationAgent:
    def __init__(self, output_dir="data"):
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)

    def run(self, context):
        print("📊 Creating visualizations...")
        df = context.get('clean_data')
        if df is None:
            raise ValueError("No clean data available for visualization")

        # Plot distribution of injuries
        plt.figure(figsize=(10, 6))
        sns.histplot(df['NUM_INJ_F'], bins=20, kde=True)
        plt.title("Distribution of Fatal Injuries")
        plot_path = os.path.join(self.output_dir, "fatal_injuries_dist.png")
        plt.savefig(plot_path)
        plt.close()

        print(f"✅ Visualization saved to {plot_path}")
        context['visual_path'] = plot_path
        return context
