from chat.chat_google_langchain import GoogleChatModelLangchain


class ChatFactory:

    @staticmethod
    def create_chat(chattype, modelname, apikey):
        match chattype:
            case ChatModelType.GOOGLE:
                return ChatFactory.create_google_chat(modelname, apikey)
            case ChatModelType.OPENAI:
                return ChatFactory.create_openai_chat(modelname, apikey)

    @staticmethod
    def create_google_chat(modelname, apikey):
        chat = GoogleChatModelLangchain(modelname, apikey)
        return chat

    @staticmethod
    def create_openai_chat(modelname, apikey):
        raise Exception("Model not implemented")


class ChatModelType:
    GOOGLE = "google"
    OPENAI = "openai"