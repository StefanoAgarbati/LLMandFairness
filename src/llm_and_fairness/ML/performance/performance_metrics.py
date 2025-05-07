from abc import ABC, abstractmethod

class MetricsNames:
    ACCURACY = 'accuracy'
    PRECISION = 'precision'
    RECALL = 'recall'
    F1 = 'f1'

class PerformanceMetrics(ABC):

    def get_metric(self, name):
        match name:
            case MetricsNames.ACCURACY:
                return self.get_accuracy()
            case MetricsNames.PRECISION:
                return self.get_precision()
            case MetricsNames.RECALL:
                return self.get_recall()
            case MetricsNames.F1:
                return self.get_f1()

    @abstractmethod
    def get_accuracy(self):
        pass

    @abstractmethod
    def get_precision(self):
        pass

    @abstractmethod
    def get_recall(self):
        pass

    @abstractmethod
    def get_f1(self):
        pass
