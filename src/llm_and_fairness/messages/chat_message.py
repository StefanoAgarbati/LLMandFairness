from abc import abstractmethod
from messages.message import Message
from tools.tool_call import ToolCall


class ChatMessage(Message):

    @abstractmethod
    def get_message(self) -> str:
        pass

    @abstractmethod
    def has_calls(self):
        pass

    @abstractmethod
    def get_tool_calls(self) -> list[ToolCall]:
        pass