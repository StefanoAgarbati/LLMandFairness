from ML.utils.performance_metrics_sklearn import PerformanceMetricsSklearn


class PerformanceMetric:
    SKLEARN = 'sklearn'


class PerformanceMetricsFactory:
    
    @staticmethod
    def create_performance_metrics(type):
        if type == PerformanceMetric.SKLEARN:
            return PerformanceMetricsSklearn()