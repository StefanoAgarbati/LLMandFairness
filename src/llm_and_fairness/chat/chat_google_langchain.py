from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

from chat.chat_model import ChatModel

from messages.chat_message_langchain import ChatMessageLangchain


class GoogleChatModelLangchain(ChatModel):

    def __init__(self, model_name, apikey):
        # os.environ['GOOGLE_API_KEY'] = apikey
        super().__init__('google')
        self.chat = ChatGoogleGenerativeAI(model=model_name, api_key=apikey)

    def sendMessage(self, amessage):
        chain = self.createChain(amessage, self.chat)
        response = chain.invoke(amessage.getParameters())
        chat_message = ChatMessageLangchain.create_message(response)
        return chat_message

    def send_message(self, message):
        response = self.chat.invoke(message)
        chat_message = ChatMessageLangchain.create_message(response)
        return chat_message

    def send_tool_message(self, message):
        print("send_tool_message: ",message.get_messages())
        response = self.chat.invoke(message.get_messages())
        return ChatMessageLangchain.create_message(response)

    def getStream(self, aMessage):
        pass

    def bind_tools(self, tools):
        tools_list = []
        for tool in tools:
            func = tool.get_as_callable()
            tools_list.append(func)
        chat_with_tools = self.chat.bind_tools(tools_list)
        self.chat = chat_with_tools

    def createPrompt(self, aMessage):
        prompt = PromptTemplate(template=aMessage.getMessageTemplate())
        return prompt

    def createChain(self, amessage, achat):
        prompt = self.createPrompt(amessage)
        chain = prompt | achat
        return chain