from applogic import LlmFairnessApplLogic
from chat import ChatModelFactory, ChatModelType
from outputdevice import OutputDeviceFactory, OutputDeviceType
from templatemessages import UserMessageRepositoryFactory


def llmFairnessMain():
    main = MainLLMFairness()
    main.startTheSystem()

class ApplConfig:
    outputDevice = OutputDeviceType.Jupyter
    apiKey = "AIzaSyCNfAQnkwlkPZbE_CTIn-GSQPks-fmQMkY"
    modelName = "gemini-2.0-flash"
    chatModelType = ChatModelType.GOOGLE


class MainLLMFairness:

    def startTheSystem(self):
        self.configureTheSystem()
        self.applLogic.activate()

    def configureTheSystem(self):
        self.messageRepository = self.createMessageRepository()
        self.chatModel = self.createChatModel()
        self.outputDevice = self.createOutputDevice()
        self.applLogic = self.createApplLogic(self.messageRepository, self.chatModel, self.outputDevice)

    def createApplLogic(self, messageRepository, chatModel, outputDevice):
        applLogic = LlmFairnessApplLogic(messageRepository, chatModel, outputDevice)
        return applLogic

    def createMessageRepository(self):
        repository = UserMessageRepositoryFactory.createUserMessageRepository()
        return repository

    def createChatModel(self):
        return ChatModelFactory.createChatModel(ApplConfig.chatModelType, ApplConfig.modelName, ApplConfig.apiKey)

    def createOutputDevice(self):
        return OutputDeviceFactory.createOutputDevice(ApplConfig.outputDevice)

