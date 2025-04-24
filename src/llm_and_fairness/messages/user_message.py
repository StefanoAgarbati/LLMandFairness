from src.llm_and_fairness.messages.message import Message
from src.llm_and_fairness.messages.prompt_support import PromptSupport


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

    def get_message(self):
        return PromptSupport.get_resolved_message(self)