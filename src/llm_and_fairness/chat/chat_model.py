from abc import ABC, abstractmethod


class ChatModel(ABC):
    @abstractmethod
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def sendMessage(self, aMessage):
        pass

    @abstractmethod
    def send_message(self, message):
        pass

    @abstractmethod
    def send_tool_message(self, message):
        pass

    @abstractmethod
    def getStream(self, aMessage):
        pass

    @abstractmethod
    def bind_tools(self, tools):
        pass