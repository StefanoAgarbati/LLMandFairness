import json
from messages import UserMessage

class UserMessageRepository:
    path = ".\messageTemplates.json"
    def __init__(self, pathname=None):
        self.messages = []
        if(pathname==None):
            self.pathname = UserMessageRepository.path
        else:
            self.pathname = pathname
        self.initRepository(self.pathname)
    def initRepository(self, pathname):
        jsonRep = json.load(open(pathname, "r"))
        templates = jsonRep['templates']
        for template in templates:
            message = template['message']
            params = template['params']
            userMessage = UserMessage(message, params)
            self.messages.append(userMessage)
    def getMessages(self):
        return self.messages
