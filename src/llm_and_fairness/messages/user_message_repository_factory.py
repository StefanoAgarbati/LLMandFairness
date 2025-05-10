import json

from messages.user_message import UserMessage
from messages.user_message_repository import UserMessageRepository


class UserMessageRepositoryFiller:
    def __init__(self, userMessageRepository, pathname=".\messageTemplates.json"):
        self.pathname = pathname
        self.repository = userMessageRepository

    def initRepository(self):
        jsonRep = json.load(open(self.pathname, "r"))
        templates = jsonRep['templates']
        for template in templates:
            message = template['message']
            params = template['params']
            tool = template['tool']
            for param in params:
                userMessage = UserMessage(message, param, tool)
                self.repository.add_user_message(userMessage)

class UserMessageRepositoryFactory:

    @staticmethod
    def createUserMessageRepository(pathname=".\messageTemplates.json"):
        repository = UserMessageRepository()
        filler = UserMessageRepositoryFiller(repository, pathname)
        filler.initRepository()
        return repository