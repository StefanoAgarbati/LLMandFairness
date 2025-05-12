from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from messages import ChatMessage


# import os
class PromptSupport:

    @staticmethod
    def getResolvedMessage(aMessage):
       return PromptTemplate(template=aMessage.getMessageTemplate()).invoke(aMessage.getParameters()).to_string()


class ChatModel:
    def __init__(self, name, chatImpl):
        self.name = name
        self.chatImpl = chatImpl

    def sendMessage(self, aMessage):
        return self.chatImpl.sendMessage(aMessage)

    def getStream(self, aMessage):
        return self.chatImpl.getStream(aMessage)

    def bind_tools(self, tools):
        self.chatImpl.bind_tools(tools)

class ChatModelImplementation:
    def __init__(self, modelName):
        self.modelName = modelName
        self.llm = self.getLLM()
        #print("ChatModelImplementation llm ", self.llm)

    def sendMessage(self, aMessage):
        chain = self.createChain(aMessage, self.llm)
        response = chain.invoke(aMessage.getParameters())
        chatMessage = ChatMessage(response.text())
        return chatMessage

    def getStream(self, aMessage):
        # chain = self.createChain(aMessage, self.llm)
        # stream = chain.stream(aMessage.getParameters())
        pass
    def bind_tools(self, tools):
        pass
    def getLLM(self):
        pass

    def createPrompt(self, aMessage):
        prompt = PromptTemplate(template=aMessage.getMessageTemplate())
        return prompt
    def createChain(self, aMessage, llm):
        prompt = self.createPrompt(aMessage)
        chain = prompt | llm
        return chain


class GoogleChatModel(ChatModelImplementation):
    def __init__(self, modelName, apikey):
        # os.environ['GOOGLE_API_KEY'] = apikey
        self.apiKey = apikey
        super().__init__(modelName)
        #print(f"GoogleChatModel cons() llm is  {self.llm}")
        #print(f"GoogleChatModel apikey {self.apiKey}")

    def bind_tools(self, tools):
        self.llm = self.llm.bind_tools(tools)

    def getLLM(self):
        #print("GoogleChatModel getLLM called")
        chat = ChatGoogleGenerativeAI(model=self.modelName, api_key=self.apiKey)
        return chat


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
        #print("ChatModelFactory createGoogleChatModel apikey", apiKey)
        googleChatImpl = GoogleChatModel(modelName, apiKey)
        chat = ChatModel('google', googleChatImpl)
        return chat

    @staticmethod
    def createOpenAIChatModel(modelName, apiKey):
        raise Exception("This model is not yet implemented")

