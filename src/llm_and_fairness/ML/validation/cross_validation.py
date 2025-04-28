from abc import ABC, abstractmethod


class CrossValidation(ABC):

    @abstractmethod
    def cross_validate_model(self, model, dataset, target, cv, scorings):
        pass