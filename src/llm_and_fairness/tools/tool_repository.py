from abc import ABC, abstractmethod



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