from ML.utils.train_test_split_sklearn import TrainTestSplitterSkLearn


class TrainTestSplitType:
    SKLEARN = 'Sklearn'


class TrainTestSplitFactory:

    @staticmethod
    def create_train_test_splitter(type):
        if type == TrainTestSplitType.SKLEARN:
            return TrainTestSplitFactory.create_train_test_split_sklearn()

    @staticmethod
    def create_train_test_split_sklearn():
        return TrainTestSplitterSkLearn()