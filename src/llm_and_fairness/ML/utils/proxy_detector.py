from abc import ABC, abstractmethod


class ProxyDetector(ABC):

    @abstractmethod
    def detect_proxy(self, dataset, variable):
        pass

