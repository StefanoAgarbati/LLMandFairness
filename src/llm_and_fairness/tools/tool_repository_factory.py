from tools.tool_repository_langchain import ToolRepositoryLangchain
from tools.tool_repository_standard import ToolRepositoryStandard


class ToolRepositoryFactory:

    @staticmethod
    def create(repository_type):
        match repository_type:
            case ToolRepositoryType.LANGCHAIN:
                return ToolRepositoryLangchain()
            case ToolRepositoryType.STANDARD:
                return ToolRepositoryStandard()
            case _:
                raise Exception("Repository type not supported")


class ToolRepositoryType:
    LANGCHAIN = 'tool_repository_langchain'
    STANDARD = 'tool_repository_standard'