from ML.encoding.encoder import Encoder
from sklearn.preprocessing import LabelEncoder

class SkLearnNominalEncoder(Encoder):

    def __init__(self):
        self.nominal_encoder = LabelEncoder()

    def encode(self, attribute):
        attribute_encoded = self.nominal_encoder.fit_transform(attribute)
        return attribute_encoded