import json


class DatasetInfo:

    def __init__(self, dataset_name):
        self.pathname = "datasets/" + dataset_name + "/" + dataset_name + "columnsencoding.json"
        self.data = []
        self.dataset_name = dataset_name
        self.init_data()

    @staticmethod
    def create(dataset_name):
        dataset_info = DatasetInfo(dataset_name)
        return dataset_info

    def get_dataset_name(self):
        return self.dataset_name

    def get_info(self):
        return self.data

    def init_data(self):
        jsonObj = json.load(open(self.pathname, "r"))
        features = jsonObj['features']
        self.data = features