from ML.split import Split
from ML.utils.train_test_split_sklearn import TrainTestSplitterSkLearn


class DatasetTrainTestSplitter:

    def __init__(self, split_repository, dataset_repository):
        self.split_repository = split_repository
        self.dataset_repository = dataset_repository
        self.splitter = None

    def split(self, dataset_name, target):
        dataset = self.dataset_repository.get_dataset_by_name(dataset_name)
        X = self.get_X_data(dataset, target)
        y = self.get_y_target(dataset, target)
        split = self.execute_split(dataset_name, X, y)
        self.split_repository.add_split(split)
        return split

    def execute_split(self, dataset_name, X, y):
        X_train, X_test, y_train, y_test = TrainTestSplitterSkLearn.split(X, y)
        split = Split(dataset_name, X_train, X_test, y_train, y_test)
        return split

    def get_X_data(self, dataset, target):
        X = dataset.drop(columns=target)
        return X

    def get_y_target(self, dataset, target):
        if len(target) == 1:
            return dataset[target[0]]
        return dataset[target]

