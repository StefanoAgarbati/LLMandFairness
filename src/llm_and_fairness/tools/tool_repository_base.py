from tools.tool_repository import ToolRepository

class ToolRepositoryBase(ToolRepository):

    def __init__(self):
        self.tools = []

    def get_tool_by_name(self, name):
        for tool in self.tools:
            tool_name = tool.get_name()
            if tool_name == name:
                return tool
        return None

    def add_tool(self, a_tool):
        self.tools.append(a_tool)

    def get_all(self):
        return self.tools


