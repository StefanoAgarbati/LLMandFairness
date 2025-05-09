from abc import ABC, abstractmethod


class FairnessMetrics(ABC):

    @abstractmethod
    def demographic_parity_difference(self, y_true, y_pred, sensitive_groups):
        pass

    @abstractmethod
    def demographic_parity_ratio(self, y_true, y_pred, sensitive_groups):
        pass

    @abstractmethod
    def by_groups(self, metrics, y_true, y_pred, sensitive_groups):
        pass

    def get_metric(self, metric_name):
        match metric_name:
            case 'selection_rate':
                return self.get_selection_rate()
            case 'accuracy':
                return self.get_accuracy()
            case _:
                raise Exception("FairnessMetrics -> The metric " + metric_name + " doesn't exist")

    @abstractmethod
    def get_selection_rate(self):
        pass

    @abstractmethod
    def get_accuracy(self):
        pass
