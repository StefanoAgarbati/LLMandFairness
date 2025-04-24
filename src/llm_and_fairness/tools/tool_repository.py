from abc import ABC, abstractmethod

from src.llm_and_fairness.tools.tool import Tool


class ToolRepository(ABC):

    @abstractmethod
    def get_tool_by_name(self, name):
        pass

    @abstractmethod
    def add_tool(self, a_tool):
        pass

    @abstractmethod
    def get_all(self):
        pass