from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from messages import ChatMessage


# import os

class ChatModel:
    def __init__(self, name, chatImpl):
        self.name = name
        self.chatImpl = chatImpl

    def sendMessage(self, aMessage):
        return self.chatImpl.sendMessage(aMessage)

    def getStream(self, aMessage):
        return self.chatImpl.getStream(aMessage)


class ChatModelImplementation:
    def __init__(self, modelName):
        self.modelName = modelName
        self.llm = self.getLLM()

    def sendMessage(self, aMessage):
        chain = self.createChain(aMessage, self.llm)
        response = chain.invoke(aMessage.getParameters())
        chatMessage = ChatMessage(response.text())
        return chatMessage

    def getStream(self, aMessage):
        # chain = self.createChain(aMessage, self.llm)
        # stream = chain.stream(aMessage.getParameters())
        pass

    def getLLM(self):
        print("ChatModelImplementation getLLM called")
        pass

    def createChain(self, aMessage, llm):
        prompt = PromptTemplate(template=aMessage.getMessageTemplate())
        chain = prompt | llm
        return chain


class GoogleChatModel(ChatModelImplementation):
    def __init__(self, modelName, apikey):
        # os.environ['GOOGLE_API_KEY'] = apikey
        super().__init__(modelName)

    def getLLM(self):
        print("GoogleChatModel getLLM called")
        chat = ChatGoogleGenerativeAI(model=self.name, api_key=apikey)
        return chat

class ChatModelConfig:
    pass


class ChatModelType:
    GOOGLE = "google"
    OPENAI = "openai"


class ChatModelFactory:

    def createChatModel(chatModelType, modelName, apiKey):
        match chatModelType:
            case ChatModelType.GOOGLE:
                return ChatModelFactory.createGoogleChatModel(modelName, apiKey)
            case ChatModelType.OPENAI:
                return ChatModelFactory.createOpenAIChatModel(modelName, apiKey)
            case _:
                raise Exception("The model type selected is not supported")

    @staticmethod
    def createGoogleChatModel(modelName, apiKey):
        googleChatImpl = GoogleChatModel(modelName, apiKey)
        chat = ChatModel('google', googleChatImpl)
        return chat

    @staticmethod
    def createOpenAIChatModel(modelName, apiKey):
        raise Exception("This model is not yet implemented")
