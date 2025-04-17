import pandas as pd
import json 

class DatasetReader:
    def __init__(self, pathname, columnspath):
        self.pathname = pathname
        self.columnspath = columnspath
        
    def load(self):
        data = self.readCsv(self.pathname)
        columnNames = json.load(open(self.columnspath, "r"))['columns']
        data.columns = columnNames
        return data

    def readCsv(self, pathname):
        data = pd.read_csv(pathname, header=None)
        return data

class DatasetLoader:
    def __init__(self, pathname, description):
        self.pathname = pathname
        self.description = json.load(open(description, 'r'))

        self.frame = pd.read_csv(pathname, header=None)
        attributes_names = self.description['columns']
        self.frame.columns = attributes_names

        if ((self.frame.columns == self.frame.loc[0,:])).all():
            self.frame = self.frame.drop(0)

    def get_data(self):
        return self.frame

    @staticmethod
    def create_dataset(pathname, description):
        dataset_loader = DatasetLoader(pathname, description)
        return dataset_loader.get_data()