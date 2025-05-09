class GetAvailableFairnessMetricsUseCase:

    def __init__(self, metrics):
        self.metrics = metrics

    def get_group_metrics(self, problem):
        return self.get_metrics(problem, 'disaggregated_metrics')

    def get_aggregated_metrics(self, problem):
        return self.get_metrics(problem, 'aggregated_metrics')

    def get_metrics(self, problem, metric_type):
        for metric in self.metrics:
            if metric['problem'] == problem:
                return metric[metric_type]
        raise Exception(f"There are no metrics for type {problem}")