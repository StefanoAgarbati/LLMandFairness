from messages.tool_execution_message import ToolExecutionMessage
from messages.tool_execution_message_langchain import ToolExecutionMessageLangchain
from tools.tool import Tool


class ToolLangchain(Tool):
    def __init__(self, a_callable, name):
        super().__init__(a_callable, name)
        self.acallable = a_callable
        self.name = name

    def get_as_callable(self):
        return self.acallable

    def get_name(self):
        return self.name

    def execute(self,tool_call) -> ToolExecutionMessage:
        result = self.acallable.invoke(tool_call)
        tool_exec_message = ToolExecutionMessageLangchain(tool_call, result)
        return tool_exec_message