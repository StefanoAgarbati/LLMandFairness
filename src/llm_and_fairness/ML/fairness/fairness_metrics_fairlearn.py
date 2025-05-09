from fairlearn.metrics import MetricFrame, selection_rate, demographic_parity_difference, demographic_parity_ratio
import sklearn.metrics as mk

from ML.fairness.fairness_metrics import FairnessMetrics


class FairnessMetricsFairlearn(FairnessMetrics):

    # def __init__(self, metrics, dataset, y_true, y_pred, sensitive_groups):
    #     self.dataset = dataset
    #     self.y_true = y_true
    #     self.y_pred = y_pred
    #     self.sensitive_groups = sensitive_groups
    #     self.metrics = self.init_metrics(metrics)
    #     self.frame = self.init_frame()

    def demographic_parity_difference(self, y_true, y_pred, sensitive_groups):
        return demographic_parity_difference(y_true, y_pred, sensitive_features=sensitive_groups)

    def demographic_parity_ratio(self, y_true, y_pred, sensitive_groups):
        return demographic_parity_ratio(y_true, y_pred, sensitive_features=sensitive_groups)

    def by_groups(self, metrics, y_true, y_pred, sensitive_groups):
        ms = self.init_metrics(metrics)
        frame = self.init_frame(ms, y_true, y_pred, sensitive_groups)
        #report = FairnessReport(sensitive_groups, metrics, frame.by_group)
        return frame.by_group

    def init_frame(self, metrics, y_true, y_pred, sensitive_groups):
        mf = MetricFrame(
            metrics=metrics,
            y_pred=y_pred,
            y_true=y_true,
            sensitive_features=sensitive_groups
        )
        return mf

    def init_metrics(self, metrics):
        ms = []
        for metric in metrics:
            metric_name = metric
            metric_function = super().get_metric(metric_name)
            ms_item = (metric_name, metric_function)
            ms.append(ms_item)
        ms_dict = dict(ms)
        return ms_dict

    def get_selection_rate(self):
        return selection_rate

    def get_accuracy(self):
        return mk.accuracy_score


