from abc import ABC, abstractmethod


class OutputDevice(ABC):

    @abstractmethod
    def out(self, aMessage):
        pass

    @abstractmethod
    def out_markdown(self, data):
        pass

    @abstractmethod
    def out_figure(self, figure):
        pass