from messages.message import Message
from messages.prompt_support import PromptSupport


class UserMessage(Message):
    def __init__(self, messageTemplate, parameters, tool=''):
        self.messageTemplate = messageTemplate
        self.parameters = parameters
        self.tool = tool

    def getMessageTemplate(self):
        return self.messageTemplate

    def getParameters(self):
        return self.parameters

    def getParameter(self, parameterName):
        if not parameterName in self.getParameters():
            raise Exception("The parameter provided is not correct")
        return self.getParameters()[parameterName]

    def get_message(self):
        return PromptSupport.get_resolved_message(self)

    def has_tool(self):
        return self.tool != ''

    def get_tool(self):
        return self.tool