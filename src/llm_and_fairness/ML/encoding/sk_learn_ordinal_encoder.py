from sklearn.preprocessing import OrdinalEncoder

from ML.encoding.encoder import Encoder


class SkLearnOrdinalEncoder(Encoder):

    def __init__(self, categories=None):
        self.encoder = OrdinalEncoder(categories=[categories])

    def encode(self, attribute):
        attribute_encoded = self.encoder.fit_transform(attribute)
        return attribute_encoded