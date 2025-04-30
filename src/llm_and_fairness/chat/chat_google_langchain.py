from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

from chat.chat_model import ChatModel
from chat.chat_model_langchain import ChatModelLangchain

from messages.chat_message_langchain import ChatMessageLangchain


class GoogleChatModelLangchain(ChatModelLangchain):

    def __init__(self, model_name, apikey):
        # os.environ['GOOGLE_API_KEY'] = apikey
        super().__init__('google', model_name, apikey)

    def create_chat(self, model_name, apikey):
        chat = ChatGoogleGenerativeAI(model=model_name, api_key=apikey)
        return chat


