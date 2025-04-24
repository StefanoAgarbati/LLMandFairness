from src.llm_and_fairness.tools.tool_langchain import ToolLangchain
from src.llm_and_fairness.tools.tool_repository_base import ToolRepositoryBase
from src.llm_and_fairness.tools import tools_functions as tf

class ToolRepositoryLangchain(ToolRepositoryBase):

    def __init__(self):
        super().__init__()
        for tool_name in tf.get_available_tools_names():
            tool = ToolLangchain(tf.get_tool_by_name(tool_name), tool_name)
            self.add_tool(tool)
