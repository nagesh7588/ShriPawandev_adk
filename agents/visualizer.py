# agents/visualizer.py
import matplotlib.pyplot as plt
import seaborn as sns
import os

class Visualizer:
    def plot_incidents(self, df):
        plt.figure(figsize=(12, 6))
        sns.countplot(x='year', data=df, hue='severity', palette='Reds')
        plt.title('Aviation Incidents by Year and Severity', fontsize=14)
        plt.xlabel('Year')
        plt.ylabel('Incident Count')
        plt.xticks(rotation=45)
        plt.tight_layout()

        os.makedirs('outputs', exist_ok=True)
        plot_path = 'outputs/incidents_plot.png'
        plt.savefig(plot_path)
        plt.close()
        return plot_path
