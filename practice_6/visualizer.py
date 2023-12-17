import seaborn as sns
import matplotlib.pyplot as plt


class Visualizer:
    @staticmethod
    def plot_heatmap(pivot_table, table_size, title, x_label, y_label):
        plt.figure(figsize=table_size)
        sns.heatmap(pivot_table, annot=True, fmt="d", cmap="YlGnBu")
        plt.title(title)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.show()
