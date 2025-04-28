from abc import abstractmethod

from ML.classification.classifier import Classifier


class RandomForestClassifier(Classifier):

    @abstractmethod
    def get_feature_importances(self):
        pass

    @abstractmethod
    def predict_probability(self, data):
        pass