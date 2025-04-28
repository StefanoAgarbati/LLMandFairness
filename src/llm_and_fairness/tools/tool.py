from abc import ABC, abstractmethod

from messages.tool_execution_message import ToolExecutionMessage


class Tool(ABC):

    @abstractmethod
    def __init__(self, a_callable, name):
        self.acallable = a_callable
        self.name = name

    def get_as_callable(self):
        return self.acallable

    def get_name(self):
        return self.name

    @abstractmethod
    def execute(self,tool_call) -> ToolExecutionMessage:
        pass