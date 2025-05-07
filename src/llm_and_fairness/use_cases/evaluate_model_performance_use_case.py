class EvaluateModelPerformanceUseCase:

    def __init__(self, performance_metrics, split_repository, prediction_repository):
        self.prediction_repository = prediction_repository
        self.split_repository = split_repository
        self.performance_metrics = performance_metrics

    def evaluate_model_performance(self, metrics_names, dataset_name):
        metrics_list = self.get_metrics_list(metrics_names)
        split = self.get_split_from_repository(dataset_name)
        prediction = self.get_prediction_from_repository(dataset_name)
        performances = self.execute_evaluation(metrics_list, split, prediction)
        return performances

    def get_metrics_list(self, metrics_names):
        return metrics_names.replace(" ", "").split(",")

    def get_split_from_repository(self, dataset_name):
        return self.split_repository.get_split_by_name(dataset_name)

    def get_prediction_from_repository(self, dataset_name):
        return self.prediction_repository.get_prediction_by_name(dataset_name)

    def execute_evaluation(self, metrics_list, split, prediction):
        performances = []
        for metric_name in metrics_list:
            metric = self.get_metric_from_name(metric_name)
            y_pred = prediction.get_y_pred()
            y_true = split.get_y_test()
            performance = {'metric_name': metric.get_name(), 'metric_value': metric.get_value(y_true, y_pred)}
            performances.append(performance)
        return performances

    def get_metric_from_name(self, metric_name):
        return self.performance_metrics.get_metric(metric_name)