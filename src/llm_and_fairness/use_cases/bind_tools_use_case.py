class BindToolsToChatUseCase:

    def __init__(self, tool_repository, a_chat):
        self.tool_repository = tool_repository
        self.chat = a_chat

    def bind_tools(self):
        all_tools = self.tool_repository.get_all()
        self.chat.bind_tools(all_tools)
