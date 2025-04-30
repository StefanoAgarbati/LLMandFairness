from sklearn.metrics import accuracy_score

from ML.utils.performance_metrics import PerformanceMetrics


class PerformanceMetricsSklearn(PerformanceMetrics):

    def get_accuracy(self, y_true, y_pred):
        return accuracy_score(y_true, y_pred)