from abc import abstractmethod

from langchain_core.prompts import PromptTemplate

from chat.chat_model import ChatModel
from messages.chat_message_langchain import ChatMessageLangchain



class ChatModelLangchain(ChatModel):
    @abstractmethod
    def __init__(self, name ,model_name, apikey):
        # os.environ['GOOGLE_API_KEY'] = apikey
        self.chat = self.create_chat(model_name, apikey)

    def sendMessage(self, amessage):
        chain = self.createChain(amessage, self.chat)
        response = chain.invoke(amessage.getParameters())
        chat_message = ChatMessageLangchain.create_message(response)
        return chat_message

    def send_message(self, message):
        response = self.chat.invoke(message)
        #print("ChatModelLangchain->response->",response.text())
        chat_message = ChatMessageLangchain.create_message(response)
        return chat_message

    def send_a_message(self, message):
        return self.send_tool_message(message, '')

    def send_tool_message(self, message, tool):
        #print(f"send_tool_message with tool {tool}")
        response = self.chat.invoke(message, config={"tool_choice": tool})
        print("ChatModelLangchain->response->", response.text())
        chat_message = ChatMessageLangchain.create_message(response, tool)
        return chat_message

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

    @abstractmethod
    def create_chat(self, model_name, apikey):
        pass