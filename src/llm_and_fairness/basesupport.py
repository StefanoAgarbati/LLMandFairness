from abc import ABC, abstractmethod
from threading import Thread

class ActiveObject(ABC,Thread):

    def __init__(self, name=''):
        super().__init__()
        self.name = name
        
    def run(self):
        self.doJob()

    def activate(self):
        super().start()

    @abstractmethod
    def doJob(self):
        pass
    
    