from ML.classification.classifier_factory import ClassifierModel, ClassifierFactory
from ML.utils.proxy_detection import ProxyDetection
from ML.utils.proxy_detector import ProxyDetector


class ProxyDetectorTreeBased(ProxyDetector):
    def __init__(self, splitter, performance_metrics):
        self.model_config = {"model": ClassifierModel.RANDOM_FOREST}
        self.splitter = splitter
        self.metrics = performance_metrics

    def detect_proxy(self, dataset, variable):
        X = self.drop_target_variable(dataset, variable)
        y = self.get_target_variable(dataset, variable)

        X_train, X_test, y_train, y_test = self.train_test_splitting(X, y)

        model = ClassifierFactory.create_classifier(self.model_config)

        model.fit(X_train, y_train)

        y_pred = model.predict(X_test)

        accuracy = self.metrics.get_accuracy(y_test, y_pred)
        feature_importance = model.get_feature_importances()

        detection = ProxyDetection({"variable_name": variable, "accuracy": accuracy, "importances": feature_importance})
        return detection

    def drop_target_variable(self, dataset, variable):
        return dataset.drop(columns=variable)

    def get_target_variable(self, dataset, variable):
        return dataset[variable]

    def train_test_splitting(self, X, y):
        return self.splitter.split(X, y)