from basesupport import ActiveObject
from chat import PromptSupport


class LlmFairnessApplLogic(ActiveObject):
    """
    -> get a message from repository to sendo to an llm
    -> waiting for response
    -> show the response given by the llm using an output device
    """
    def __init__(self, aMessageRepository, aChatModel, anOutputDevice):
        super().__init__('applLogic')
        self.aMessageRepository = aMessageRepository
        self.aChatModel = aChatModel
        self.anOutputDevice = anOutputDevice

    def executeLogic(self):
        messages = self.aMessageRepository.getMessages()
        for message in messages:
           self.processMessage(message)

    def sendMessageToLLM(self, message):
       return self.aChatModel.sendMessage(message)

    def processMessage(self, message):
        self.showQuestion(PromptSupport.getResolvedMessage(message))
        response = self.sendMessageToLLM(message)
        self.showResponse(response.getMessage())

    def showQuestion(self, aMessage):
        self.anOutputDevice.out(aMessage)
        self.anOutputDevice.out("")

    def showResponse(self, aMessage):
        self.anOutputDevice.out(aMessage)
        self.anOutputDevice.out("")
        self.anOutputDevice.out("")

    def doJob(self):
        self.executeLogic()
