from abc import abstractmethod

from ML.classification.classifier import Classifier


class EnsembleClassifier(Classifier):

    def __init__(self, classifier, name):
        super().__init__(name)
        self.classifier = classifier
        self.features = None

    def get_feature_importances(self):
        if self.features is None:
            raise Exception(self.name + " -> The classifier has not been trained yet")
        importances = self.get_importances(self.classifier.feature_importances_, self.features)
        return importances

    def predict_probability(self, data):
        y_pred = self.classifier.predict_proba(data)
        return y_pred

    def fit(self, data_train, target_train):
        self.features = data_train.columns
        self.classifier.fit(data_train, target_train)
        return self

    def predict(self, data_test):
        y_pred = self.classifier.predict(data_test)
        return y_pred

    @abstractmethod
    def get_importances(self, importances, features):
        pass
        #return pd.Series(importances, index=features).sort_values(ascending=False)
