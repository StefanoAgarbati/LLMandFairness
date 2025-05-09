
import sklearn.ensemble as ske
import pandas as pd

from ML.classification.ensemble_classifier import EnsembleClassifier


class GradientBoostingClassifierSklearn(EnsembleClassifier):

    def __init__(self, name):
        self.name = name
        self.classifier = ske.GradientBoostingClassifier(random_state=42)
        self.features = None
        super().__init__(self.classifier, self.name)


    def get_importances(self, importances, features):
        return pd.Series(importances, index=features).sort_values(ascending=False)

    def get_model(self):
        return self.classifier