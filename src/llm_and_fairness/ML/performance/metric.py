from abc import ABC, abstractmethod


class Metric:

    def __init__(self, metric_name, metrics_function):
        self.name = metric_name
        self.function = metrics_function

    def get_name(self):
        return self.name

    def get_value(self, y_true, y_pred):
        result = self.function(y_true, y_pred)
        return result
