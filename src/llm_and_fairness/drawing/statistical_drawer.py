from abc import ABC, abstractmethod


class StatisticalDrawer(ABC):

    @abstractmethod
    def countplot(self, data, x_var, order=None):
        pass

    @abstractmethod
    def histplot(self, data, x_var):
        pass

    @abstractmethod
    def heatmap(self, data, figsize=None, fmt=None, colormap=None):
        pass

