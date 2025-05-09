from messages.tool_execution_message import ToolExecutionMessage
from messages.tool_execution_message_impl import ToolExecutionMessageImpl
from tools.tool import Tool


class ToolLocal(Tool):

    def __init__(self, a_callable, name):
        super().__init__(a_callable, name)

    def execute(self, tool_call) -> ToolExecutionMessage:
        args = tool_call['args']
        result = self.acallable(**args)
        tool_exec_message = ToolExecutionMessageImpl(tool_call, result)
        return tool_exec_message
