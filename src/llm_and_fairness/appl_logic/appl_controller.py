import time

from basesupport import ActiveObject
from messages.user_message import UserMessage


class ApplController(ActiveObject):

    def __init__(self, add_memory_use_case, get_memories_use_case, display_use_case, handle_response_use_case,
                 send_message_use_case, get_user_message_use_case
                 ):
        super().__init__('ApplLogic')
        self.send_message_uc = send_message_use_case
        self.handle_response_uc = handle_response_use_case
        self.display_use_case = display_use_case
        self.get_memories_uc = get_memories_use_case
        self.add_memory_uc = add_memory_use_case
        self.get_user_message_use_case = get_user_message_use_case
        self.messages = []
        self.init_messages()

    def execute(self):
        for message in self.messages:
            self.execute_step(message)

    def execute_step(self, message):
        self.process_message(message)
        time.sleep(15)

    def process_message(self, message):
        self.add_memory(message.get_message())
        self.show_request(message)
        memories = self.get_memories()
        #print("Memories:" , memories)
        response = self.send_memory_to_chat(memories)
        responses = self.handle_response(response)
        self.show_response(responses)
        self.add_memories(responses)

    def show_request(self, message):
        self.display_use_case.display_request(message)

    def show_response(self, responses):
        for response in responses:
            self.display_use_case.display_response(response)

    def add_memory(self, message):
        self.add_memory_uc.add_memory(message)

    def get_memories(self):
        return self.get_memories_uc.get_memories()

    def send_memory_to_chat(self, memories):
        return self.send_message_uc.send_string_message(memories)

    def handle_response(self, response):
        return self.handle_response_uc.handle(response)

    """def show_message(self, message):
        self.output_device.out(message)"""

    def doJob(self):
        self.execute()

    def init_messages(self):
        self.messages = self.get_user_message_use_case.get_user_messages()

    def add_memories(self, memories):
        self.add_memory_uc.add_memories(memories)

