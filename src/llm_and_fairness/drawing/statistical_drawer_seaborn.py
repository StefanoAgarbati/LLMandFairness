import matplotlib.pyplot as plt

from drawing.statistical_drawer import StatisticalDrawer
import seaborn as sns

class StatisticalDrawerSeaborn(StatisticalDrawer):

    def histplot(self, data, x_var):
        fig, axs = plt.subplots()
        ax = sns.histplot(data, x=x_var, ax=axs)
        plt.close()
        return fig

    def countplot(self, data, x_var, order=None):
        fig, axs = plt.subplots()
        ax = sns.countplot(data, x=x_var, order=order, ax=axs)
        ax.tick_params(axis='x', rotation=90)
        plt.close()
        return fig

    def heatmap(self, data, figsize=None, fmt=None, annot=True, colormap=None):
        fig, axs = plt.subplots(figsize=figsize)
        ax = sns.heatmap(data, fmt=fmt, annot=annot, cmap=colormap)
        plt.close()
        return fig
