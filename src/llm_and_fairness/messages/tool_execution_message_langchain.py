from messages.tool_execution_message import ToolExecutionMessage


class ToolExecutionMessageLangchain(ToolExecutionMessage):

    def __init__(self, tool_call, result):
        self.result = result
        self.tool_call = tool_call

    def get_tool_name(self):
        return self.tool_call['name']

    def get_args(self):
        return self.tool_call['args']

    def get_content(self):
        return self.result.content

    def get_artifact(self):
        return self.result.artifact

    def get_result(self):
        return self.result

    def get_message(self):
        return self.get_content()