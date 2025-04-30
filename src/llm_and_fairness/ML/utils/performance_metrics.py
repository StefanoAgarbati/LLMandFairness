from abc import ABC, abstractmethod


class PerformanceMetrics(ABC):

    @abstractmethod
    def get_accuracy(self, y_true, y_pred):
        pass



