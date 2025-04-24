from src.llm_and_fairness.chat.chat_model import ChatModel


class SendMessageUseCase:

    def __init__(self, achat):
        self.chat = achat

    def send_message(self, amessage):
        chat_message_response = self.chat.sendMessage(amessage)
        #self.response_handler.handle(chat_message_response)
        return chat_message_response

    def send_string_message(self, message):
        chat_message_response = self.chat.send_message(message)
        return chat_message_response



