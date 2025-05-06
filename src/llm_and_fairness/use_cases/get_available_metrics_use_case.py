from ML.MLProblemType import MLProblemType


class GetAvailableMetricsUseCase:

    def __init__(self, metrics):
        self.metrics = metrics

    def get_available_metrics_for(self, problem_type):
        print(f"GetAvailableMetrics: -> problem_type {problem_type}")
        for metric in self.metrics:
            if metric['problem'] == problem_type:
                return metric['metrics']
        raise Exception(f"There are no metrics for type {problem_type}")
