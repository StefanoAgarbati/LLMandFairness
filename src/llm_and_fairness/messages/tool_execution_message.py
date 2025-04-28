from abc import abstractmethod

from messages.message import Message


class ToolExecutionMessage(Message):

    @abstractmethod
    def get_tool_name(self):
        pass

    @abstractmethod
    def get_args(self):
        pass

    @abstractmethod
    def get_message(self):
        return self.get_content()

    @abstractmethod
    def get_content(self):
        pass

    @abstractmethod
    def get_artifact(self):
        pass

    @abstractmethod
    def get_result(self):
        pass