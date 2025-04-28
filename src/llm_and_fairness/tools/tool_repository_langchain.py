from tools.tool_langchain import ToolLangchain
from tools.tool_repository_base import ToolRepositoryBase
from tools import tools_functions as tf

class ToolRepositoryLangchain(ToolRepositoryBase):

    def __init__(self):
        super().__init__()
        for tool_name in tf.get_available_tools_names():
            tool = ToolLangchain(tf.get_tool_by_name(tool_name), tool_name)
            #print(f"ToolRepositoryLangchain: {tool.get_as_callable()} ")
            self.add_tool(tool)
