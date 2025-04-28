from ML.classification.classifier_factory import ClassifierFactory
from ML.prediction import Prediction


class FitPredictModelUseCase:

    def __init__(self, classifier, split_repository, prediction_repository):
        self.classifier = classifier #e se fosse un regressore o altro?
        self.split_repository = split_repository
        self.prediction_repository = prediction_repository

    def fit_predict(self, x_test_name):
        split = self.split_repository.get_split_by_name(x_test_name)
        x_test = split.get_X_test()
        x_train = split.get_X_train()
        y_train = split.get_y_train()
        fitted_classifier = self.classifier.fit(x_train, y_train)
        y_pred = self.classifier.predict(x_test)
        prediction = Prediction(x_test_name, y_pred)
        self.prediction_repository.add_prediction(prediction)
        return prediction

    def fit_and_predict(self, model_name, x_test_name):
        self.classifier = ClassifierFactory.create_classifier({"model": model_name})
        return self.fit_predict(x_test_name)