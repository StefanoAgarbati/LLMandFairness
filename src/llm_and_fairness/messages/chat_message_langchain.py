from messages.chat_message import ChatMessage
from tools.tool_call import ToolCall
from utils.string_parsing_utils import StringParsingUtils


class ChatMessageLangchain(ChatMessage):

    def __init__(self, ai_message, tool_calls=''):
        self.ai_message = ai_message
        self.tool_calls = tool_calls
        self.tool_calls_error = False

    def has_calls(self):
        #return len(self.get_tool_calls()) != 0
        return self.tool_calls != ''

    def has_calls_error(self):
        return self.tool_calls_error

    @staticmethod
    def create_message(aimessage, tool=''):
        msg = ChatMessageLangchain(aimessage, tool)
        return msg

    def get_message(self) -> str:
        return self.ai_message.text()

    def get_tool_calls(self) -> list[ToolCall]:
        if not self.has_calls():
            return []
        calls = []
        msg = self.get_message()
        #print("get_tool_calls->msg->",msg)
        tools = StringParsingUtils.from_json_to_dict(msg)
        for call in tools['tool_calls']:
            tc = ToolCall(call)
            calls.append(tc)
        return calls

    """nuova versione del metodo che esegue il parsing della stringa restituita dall'LLM
    def get_tool_calls(self) -> list[ToolCall]:
        if not self.has_calls():
            return []
        calls = []
        msg = self.get_message()
        tool_list = StringParsingUtils.from_string_to_list(msg)
        for tool in tool_list:
            call = StringParsingUtils.from_function_string_to_dict(tool)
            tc = ToolCall(call)
            calls.append(tc)
        return calls"""

    """def get_tool_calls(self) -> list[ToolCall]:
        calls = self.ai_message.tool_calls
        #print(f"ChatMessageLangchain tool calls: -> {calls}")
        tool_calls = []
        for call in calls:
            tc = ToolCall(call)
            tool_calls.append(tc)
        return tool_calls"""

    def set_tool_calls_error(self, is_error):
        self.tool_calls_error = True

