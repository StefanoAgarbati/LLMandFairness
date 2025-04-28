from abc import abstractmethod, ABC


class TrainTestSplitter(ABC):

    @staticmethod
    @abstractmethod
    def split(data, target, test_size=0.25):
        pass