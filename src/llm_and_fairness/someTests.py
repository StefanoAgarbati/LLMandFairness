from chat import GoogleChatModel, ChatModelFactory, ChatModelType
from main import ApplConfig

chat = ChatModelFactory.createChatModel(ChatModelType.GOOGLE, ApplConfig.modelName, ApplConfig.apiKey)
print(chat)

