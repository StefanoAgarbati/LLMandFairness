from ML.classification.ensemble_classifier import EnsembleClassifier

import sklearn.ensemble as ske
import pandas as pd

class RandomForestClassifierSklearn(EnsembleClassifier):

    def __init__(self, name):
        self.name = name
        self.classifier = ske.RandomForestClassifier(random_state=35)
        self.features = None
        super().__init__(self.classifier, self.name)

    def get_importances(self, importances, features):
        return pd.Series(importances, index=features).sort_values(ascending=False)

    def get_model(self):
        return self.classifier