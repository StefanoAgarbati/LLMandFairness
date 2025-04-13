class Message:
    pass


class UserMessage(Message):
    def __init__(self, messageTemplate, parameters):
        self.messageTemplate = messageTemplate
        self.parameters = parameters

    def getMessageTemplate(self):
        return self.messageTemplate

    def getParameters(self):
        return self.parameters

    def getParameter(self, parameterName):
        if not parameterName in self.getParameters():
            raise Exception("The parameter provided is not correct")
        return self.getParameters()[parameterName]


class ChatMessage(Message):
    def __init__(self, aMessage):
        self.message = aMessage

    def getMessage(self):
        return self.message


class SystemMessage(Message):
    def __init__(self, aMessage):
        self.message = aMessage
