class GetUserMessagesUseCase:

    def __init__(self, user_message_repository):
        self.user_message_repository = user_message_repository

    def get_user_messages(self):
        return self.user_message_repository.get_messages()
