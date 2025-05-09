from ML.fairness.fairness_metrics_fairlearn import FairnessMetricsFairlearn


class FairnessMetricsFactory:

    @staticmethod
    def create_fairness_metrics(name):
        if name == 'fairlearn':
            return FairnessMetricsFactory.create_fairlearn_fairness_metrics()

    @staticmethod
    def create_fairlearn_fairness_metrics():
        return FairnessMetricsFairlearn()