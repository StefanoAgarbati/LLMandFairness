from ML.encoding.encoder import Encoder
from sklearn.preprocessing import LabelEncoder
import pandas as pd

class SkLearnNominalEncoder(Encoder):

    def __init__(self):
        self.nominal_encoder = LabelEncoder()

    def encode(self, attribute):
        attribute_encoded = self.nominal_encoder.fit_transform(attribute)
        return attribute_encoded

    def decode(self, column):
        return self.nominal_encoder.inverse_transform(column)