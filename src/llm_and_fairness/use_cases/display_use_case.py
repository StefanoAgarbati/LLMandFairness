from messages.chat_message import ChatMessage
from messages.tool_execution_message import ToolExecutionMessage
from messages.user_message import UserMessage
from tools.tool_names import ToolNames


class DisplayUseCase:

    def __init__(self, output_device):
        self.output_device = output_device

    def display_request(self, request):
        if isinstance(request, UserMessage):
            msg = request.get_message()
            self.output_device.out_markdown(MessageFormattingUtils.bold_markdown(msg))

    def display_response(self, response):
        if isinstance(response, ChatMessage):
            msg = response.get_message()
            self.output_device.out_markdown(msg)

    def display_figure(self, figure):
        self.output_device.out_figure(figure)

    def display(self, data):
        self.output_device.out(data)

class MessageFormattingUtils:

    @staticmethod
    def bold_markdown(string_message):
        return "**" + string_message + "**"