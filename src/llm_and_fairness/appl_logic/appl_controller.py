import time

from src.llm_and_fairness.messages.user_message import UserMessage


class ApplController:

    def __init__(self, add_memory_use_case, get_memories_use_case, output_device, handle_response_use_case,
                 send_message_use_case
                 ):
        self.send_message_uc = send_message_use_case
        self.handle_response_uc = handle_response_use_case
        self.output_device = output_device
        self.get_memories_uc = get_memories_use_case
        self.add_memory_uc = add_memory_use_case
        self.messages = []
        self.init_messages()

    def execute(self):
        for message in self.messages:
            self.execute_step(message)

    def execute_step(self, message):
        self.process_message(message)
        time.sleep(5)

    def process_message(self, message):
        self.add_memory(message.get_message())
        self.show_message(message.get_message())
        memories = self.get_memories()
        #print("Memories:" , memories)
        response = self.send_memory_to_chat(memories)
        responses = self.handle_response(response)
        self.show_response(responses)
        self.add_memories(responses)

    def show_response(self, responses):
        for response in responses:
            self.show_message(response.get_message())

    def add_memory(self, message):
        self.add_memory_uc.add_memory(message)

    def get_memories(self):
        return self.get_memories_uc.get_memories()

    def send_memory_to_chat(self, memories):
        return self.send_message_uc.send_string_message(memories)

    def handle_response(self, response):
        return self.handle_response_uc.handle(response)

    def show_message(self, message):
        self.output_device.out(message)

    def init_messages(self):
        self.messages.append(UserMessage("Ciao, io sono Stefano", {}))
        self.messages.append(UserMessage("Carica il dataset adult", {}))
        self.messages.append(UserMessage("Calcola la distribuzione dell'attributo sex del dataset adult", {}))
        self.messages.append(UserMessage("Calcola la distribuzione dell'attributo income del dataset adult", {}))
        self.messages.append(UserMessage("Calcola la distribuzione dell'attributo occupation del dataset adult", {}))
        self.messages.append(UserMessage("Puoi dirmi se esistono disproporzioni, sbilaciamenti, bias negli attributi?", {}))
        #self.messages.append(UserMessage("Non ricordo il mio nome, sai come mi chiamo?", {}))
        #self.messages.append(UserMessage("ricordi se il mio dataset ha l'attributo sex?",{}))
        #self.messages.append(UserMessage("ricordi quali valori può assumere l'attributo sex del mio dataset?", {}))

    def add_memories(self, memories):
        self.add_memory_uc.add_memories(memories)
