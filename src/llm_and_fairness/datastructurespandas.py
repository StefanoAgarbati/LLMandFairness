import pandas as pd

from datastructures import Dataset, RangeIndex, Index

class PandasDataset(Dataset):

    def __init__(self, dataset):
        self.dataset = dataset

    def index(self):
        index = self.dataset.index
        if isinstance(index, pd.RangeIndex):
            return PandasRangeIndex(index)
        elif isinstance(index, pd.Index):
            return PandasIndex(index)
        return None

    def loc_column(self, columnsname):
        cols = self.dataset.loc[:, columnsname]


    def loc_index(self, indexes):
        pass

    def columns(self):
        pass

    def replace(self, toreplace, value):
        ds = self.dataset.replace(toreplace, value)
        return PandasDataset(ds)

class PandasRangeIndex(RangeIndex):
    def __init__(self, index):
        self.index = index

class PandasIndex(Index):
    def __init__(self, index):
        self.index = index