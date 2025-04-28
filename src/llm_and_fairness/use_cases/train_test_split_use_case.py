from ML.utils.DatasetTrainTestSplitter import DatasetTrainTestSplitter


class TrainTestSplitUseCase:

    """def __init__(self, split_repository, dataset_splitter, target, dataset_repository):
        self.split_repository = split_repository
        self.dataset_repository = dataset_repository
        self.dataset_splitter = dataset_splitter
        self.target = target"""
    def __init__(self, split_repository, dataset_repository):
        self.split_repository = split_repository
        self.dataset_repository = dataset_repository
        self.splitter = DatasetTrainTestSplitter(split_repository, dataset_repository)

    def split(self,dataset_name, target):
        return self.splitter.split(dataset_name, target)

    """def split_dataset(self, dataset_name):
       return self.split(dataset_name, self.target)

    def get_X_data(self,dataset, target):
        X = dataset.drop(columns=self.target)
        return X

    def get_y_target(self, dataset, target):
        if len(target) == 1:
            return dataset[target[0]]
        return dataset[target]"""
