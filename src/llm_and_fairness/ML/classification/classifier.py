from abc import ABC, abstractmethod


class Classifier(ABC):

    @abstractmethod
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def fit(self, data_train, target_train):
        pass

    @abstractmethod
    def predict(self, data_test):
        pass

    def get_model_name(self):
        return self.name