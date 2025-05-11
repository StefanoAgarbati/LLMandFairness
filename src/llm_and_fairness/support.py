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

        self.frame = pd.read_csv(pathname, sep=self.description['separator'], header=None, low_memory=False)
        self.frame_with = pd.read_csv(pathname, sep=self.description['separator'])
        attributes_names = self.description['columns']
        self.frame.columns = attributes_names

        if list(self.frame.columns) == self.frame.loc[0].to_list():
            self.frame = self.frame.drop(0)
            self.frame.index = range(0, self.frame.shape[0])
            for column in self.frame.columns:
                self.frame[column] = self.frame[column].astype(self.frame_with[column].dtype)

    def get_data(self):
        return self.frame

    @staticmethod
    def create_dataset(pathname, description):
        dataset_loader = DatasetLoader(pathname, description)
        return dataset_loader.get_data()


class DatasetFactory:
    #datapath = "src/llm_and_fairness/datasets/name/name.data"
    datapath = "datasets/name/name.data"
    columnspath = "datasets/name/namecolumns.json"

    @staticmethod
    def create_dataset(name):
        path = DatasetFactory.datapath.replace("name", name)
        colpath = DatasetFactory.columnspath.replace("name", name)
        dataset = DatasetLoader.create_dataset(path, colpath)
        return dataset
