from abc import ABC, abstractmethod

class Dataset(ABC):

    @abstractmethod
    def columns(self):
        pass

    @abstractmethod
    def index(self):
        pass

    @abstractmethod
    def loc_column(self,columnsname):
        pass

    @abstractmethod
    def loc_index(self, indexes):
        pass

    @abstractmethod
    def replace(self, toreplace, value):
        pass

class Serie(ABC):

    @abstractmethod
    def type(self):
        pass

    @abstractmethod
    def str(self):
        pass

class Index(ABC):
    pass
class RangeIndex(ABC):
    pass

class StringFunctions(ABC):

    @abstractmethod
    def strip(self):
        pass