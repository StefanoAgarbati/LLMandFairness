import numpy as np

class WhitespaceRemover:
    def __init__(self, dataset):
        self.dataset = dataset

    def execute(self):
        ds = self.dataset.copy()
        for column in self.dataset.columns:
            if self.dataset[column].dtype == 'object':
                ds[column] = ds[column].str.strip()
        return ds

class MissingValueDetector:
    def __init__(self, dataset, placeholders):
        self.dataset = dataset
        self.placehoders = placeholders

    def execute(self):
        pass

class ReplaceMissingValues:
    def __init__(self, dataset, placeholders):
        self.dataset = dataset
        self.placehoders = placeholders

    def execute(self):
        return self.dataset.replace(self.placehoders, np.nan)

