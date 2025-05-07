from ML.models.models_factory import ModelsFactory
from ML.prediction import Prediction


class TrainModelAndMakePrediction:

    def __init__(self, split_repository, prediction_repository):
        self.split_repository = split_repository
        self.prediction_repository = prediction_repository

    def fit_predict(self, model_name, split_name):
        model = self.create_model(model_name)
        split = self.get_split_from_repository(split_name)
        self.fit_model(model, split.get_X_train(), split.get_y_train())
        prediction = self.make_prediction(model, split.get_X_test(), split_name)
        self.add_prediction_to_repository(prediction)
        return prediction

    def create_model(self, model_name):
        return ModelsFactory.create_model(model_name)

    def get_split_from_repository(self, split_name):
        return self.split_repository.get_split_by_name(split_name)

    def fit_model(self, model, X_train, y_train):
        return model.fit(X_train, y_train)

    def make_prediction(self, model, X_test, split_name):
        y_pred = model.predict(X_test)
        return Prediction(split_name, y_pred)

    def add_prediction_to_repository(self, prediction):
        self.prediction_repository.add_prediction(prediction)


