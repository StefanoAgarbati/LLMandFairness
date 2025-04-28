import matplotlib.pyplot as plt

from drawing.statistical_drawer import StatisticalDrawer
import seaborn as sns

class StatisticalDrawerSeaborn(StatisticalDrawer):

    def histplot(self, data, x_var):
        ax = sns.histplot(data, x=x_var)
        return ax.figure

    def countplot(self, data, x_var, order=None):
        ax = sns.countplot(data, x=x_var, order=order)
        ax.tick_params(axis='x', rotation=90)
        return ax.figure

    def heatmap(self, data, figsize=None, fmt=None, annot=True, colormap=None):
        plt.figure(figsize=figsize)
        ax = sns.heatmap(data, fmt=fmt, annot=annot, cmap=colormap)
        return ax.figure
