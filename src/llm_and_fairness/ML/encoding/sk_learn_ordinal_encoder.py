import pandas as pd
from sklearn.preprocessing import OrdinalEncoder

from ML.encoding.encoder import Encoder


class SkLearnOrdinalEncoder(Encoder):

    def __init__(self, categories=None):
        self.encoder = OrdinalEncoder(categories=[categories])

    def encode(self, attribute):
        attribute_encoded = self.encoder.fit_transform(pd.DataFrame(attribute))
        return attribute_encoded.ravel()

    def decode(self, column):
        return self.encoder.inverse_transform(pd.DataFrame(column)).ravel()