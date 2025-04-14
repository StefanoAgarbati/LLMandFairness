import json
from messages import UserMessage


class UserMessageRepository:
    def __init__(self):
        self.messages = []

    def addUserMessage(self, aMessage):
        self.messages.append(aMessage)

    def getMessages(self):
        return self.messages


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

