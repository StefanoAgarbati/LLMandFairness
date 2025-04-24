import json

from src.llm_and_fairness.messages.user_message import UserMessage
from src.llm_and_fairness.messages.user_message_repository import UserMessageRepository


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
            for param in params:
                userMessage = UserMessage(message, param)
                self.repository.addUserMessage(userMessage)

class UserMessageRepositoryFactory:

    @staticmethod
    def createUserMessageRepository():
        repository = UserMessageRepository()
        filler = UserMessageRepositoryFiller(repository)
        filler.initRepository()
        return repository