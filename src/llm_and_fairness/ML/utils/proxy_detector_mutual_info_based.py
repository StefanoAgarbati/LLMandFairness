from ML.utils.mutual_info_utils import MutualInfoUtils
from ML.utils.proxy_detection import ProxyDetection
from ML.utils.proxy_detector import ProxyDetector


class ProxyDetectorMutualInfoBased(ProxyDetector):
    def __init__(self, performance_metrics):
        self.metrics = performance_metrics

    def detect_proxy(self, dataset, variable):
        X = self.drop_target_variable(dataset, variable)
        y = self.get_target_variable(dataset, variable)

        mi = MutualInfoUtils.get_mutual_info(X, y)

        detection = ProxyDetection({"variable_name": variable, "mutual_info": mi})
        return detection

    def drop_target_variable(self, dataset, variable):
        return dataset.drop(columns=variable)

    def get_target_variable(self, dataset, variable):
        return dataset[variable]

