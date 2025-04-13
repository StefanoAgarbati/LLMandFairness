import pandas as pd
import json

class DatasetLoader:
    def __init__(self, pathname, description):
        self.pathname = pathname
        self.description = json.load(open(description, 'r'))

        self.frame = pd.read_csv(pathname, header=None)
        attributes_names = self.description['names']
        self.frame.columns = attributes_names

        if ((self.frame.columns == self.frame.loc[0,:])).all():
            self.frame = self.frame.drop(0)

    def get_data(self):
        return self.frame

    def create_dataset(pathname, description):
        dataset_loader = DatasetLoader(pathname, description)
        return dataset_loader.get_data()


class AttributeDescription:
    def __init__(self, name, description, type, values):
        self.get_name(name)
        self.description = description
        self.type = type
        self.values = values

    def get_name(self):
        return self.name
    def get_description(self):
        return self.description
    def get_type(self):
        return self.type
    def get_values(self):
        return self.values

class AttributeType:
    CATEGORICAL_NOMINAL = 0
    CATEGORICAL_ORDINAL = 1
    NUMERIC = 2
