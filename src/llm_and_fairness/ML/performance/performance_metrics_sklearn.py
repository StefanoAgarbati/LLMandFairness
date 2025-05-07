import sklearn.metrics as sk

from ML.performance.metric import Metric
from ML.performance.performance_metrics import PerformanceMetrics, MetricsNames


class PerformanceMetricsSklearn(PerformanceMetrics):

    def get_accuracy(self):
        return Metric(MetricsNames.ACCURACY, sk.accuracy_score)

    def get_precision(self):
        return Metric(MetricsNames.PRECISION, sk.precision_score)

    def get_recall(self):
        return Metric(MetricsNames.RECALL, sk.recall_score)

    def get_f1(self):
        return Metric(MetricsNames.F1, sk.f1_score)