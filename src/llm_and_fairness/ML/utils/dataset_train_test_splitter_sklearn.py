from ML.utils.DatasetTrainTestSplitter import DatasetTrainTestSplitter
from ML.utils.train_test_split_sklearn import TrainTestSplitterSkLearn


class DatasetTrainTestSplitterSklearn(DatasetTrainTestSplitter):

    def create_low_level_splitter(self):
        return TrainTestSplitterSkLearn()