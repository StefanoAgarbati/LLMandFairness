class UserMessageRepository:
    def __init__(self):
        self.messages = []

    def add_user_message(self, amessage):
        self.messages.append(amessage)

    def get_messages(self):
        return self.messages