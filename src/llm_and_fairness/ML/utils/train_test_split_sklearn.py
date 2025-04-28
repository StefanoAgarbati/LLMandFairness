from sklearn.model_selection import train_test_split

from ML.utils.train_test_split import TrainTestSplitter


class TrainTestSplitterSkLearn(TrainTestSplitter):

    @staticmethod
    def split(data, target, test_size=0.25):
        X_train, X_test, y_train, y_test = train_test_split(data, target, test_size=test_size)
        return X_train, X_test, y_train, y_test



