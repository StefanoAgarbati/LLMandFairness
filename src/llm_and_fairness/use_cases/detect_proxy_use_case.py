class DetectProxyUseCase:
    
    def __init__(self, dataset_repository, proxy_detector):
        self.dataset_repository = dataset_repository
        self.proxy_detector = proxy_detector

    def detect_proxy_variables(self, dataset_name):
        dataset = self.dataset_repository.get_dataset_by_name(dataset_name)
        detections = []
        for variable in dataset.columns:
            detection = self.detect_proxy(dataset, variable)
            detections.append(detection)
        return detections

    def detect_proxy(self, dataset, variable):
       return self.proxy_detector.detect_proxy(dataset, variable)
