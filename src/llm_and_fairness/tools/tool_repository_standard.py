from tools.tool_local import ToolLocal
from tools.tool_repository_base import ToolRepositoryBase
import tools.toolkit as tk

class ToolRepositoryStandard(ToolRepositoryBase):

    def __init__(self):
        super().__init__()
        for tool_name in tk.get_available_tools_names():
            tool = ToolLocal(tk.get_tool_by_name(tool_name), tool_name)
            #print(f"ToolRepositoryLangchain: {tool.get_as_callable()} ")
            self.add_tool(tool)