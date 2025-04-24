from src.llm_and_fairness.messages.chat_message import ChatMessage
from src.llm_and_fairness.tools.tool_call import ToolCall


class ChatMessageLangchain(ChatMessage):

    def __init__(self, ai_message):
        self.ai_message = ai_message

    def has_calls(self):
        return len(self.get_tool_calls()) != 0

    @staticmethod
    def create_message(aimessage):
        msg = ChatMessageLangchain(aimessage)
        return msg

    def get_message(self) -> str:
        return self.ai_message.text()

    def get_tool_calls(self) -> list[ToolCall]:
        calls = self.ai_message.tool_calls
        tool_calls = []
        for call in calls:
            tc = ToolCall(call)
            tool_calls.append(tc)
        return tool_calls
