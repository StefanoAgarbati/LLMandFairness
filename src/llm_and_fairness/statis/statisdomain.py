from abc import ABC, abstractmethod

class Distribution:
    def __init__(self, name, distribution_data):
        self.name = name
        self.data = distribution_data

    def get_name(self):
        return self.name

    def get_data(self):
        return self.data

class StatisticsSupport(ABC):
    
    @abstractmethod
    def get_distribution(self, name, distribution_type):
        pass