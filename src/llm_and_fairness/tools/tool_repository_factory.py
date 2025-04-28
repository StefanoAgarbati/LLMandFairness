from tools.tool_repository_langchain import ToolRepositoryLangchain

class ToolRepositoryFactory:

    @staticmethod
    def create(repository_type):
        match repository_type:
            case ToolRepositoryType.LANGCHAIN:
                return ToolRepositoryLangchain()
            case _:
                raise Exception("Repository type not supported")


class ToolRepositoryType:
    LANGCHAIN = 'tool_repository_langchain'