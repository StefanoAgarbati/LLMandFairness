from abc import abstractmethod
from src.llm_and_fairness.messages.message import Message
from src.llm_and_fairness.tools.tool_call import ToolCall


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