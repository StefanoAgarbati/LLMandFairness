from abc import ABC, abstractmethod

class Encoder(ABC):

    @abstractmethod
    def encode(self, column):
        pass

    @abstractmethod
    def decode(self, column):
        pass