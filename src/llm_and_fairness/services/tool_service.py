class ToolService:

    def __init__(self, tool_repository):
        self.tool_repository = tool_repository

    def add_a_tool(self, atool):
        self.tool_repository.add_tool(atool)

