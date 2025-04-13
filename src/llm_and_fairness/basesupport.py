from threading import Thread

class ActiveObject(Thread):

    def __init__(self, name=''):
        super().__init__()
        self.name = name
        
    def run(self):
        self.doJob()

    def activate(self):
        super().start()

    def doJob(self):
        pass
    
    