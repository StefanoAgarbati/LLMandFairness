from operator import truediv


class DatasetRepository:

    def __init__(self):
        self.datasets = []

    def has_dataset(self, name):
        for dataset in self.datasets:
            if dataset['name'] == name:
                return True
        return False

    def add_dataset(self, name, dataset):
        self.datasets.append({
            "name": name,
            "data": dataset
        })
        #print(f"DatasetRepository - dataset added -> {name}, {dataset}")

    def get_dataset_by_name(self, name):
        for dataset in self.datasets:
            if not self.has_dataset(name):
                raise Exception("The dataset does not exist")
            if dataset['name'] == name:
                return dataset['data']

