import time

from messages.user_message import UserMessage


class ApplControllerTest:

    def __init__(self, add_memory_use_case, get_memories_use_case, display_use_case, handle_response_use_case,
                 send_message_use_case
                 ):
        self.send_message_uc = send_message_use_case
        self.handle_response_uc = handle_response_use_case
        self.display_use_case = display_use_case
        self.get_memories_uc = get_memories_use_case
        self.add_memory_uc = add_memory_use_case
        self.messages = []
        self.init_messages()

    def execute(self):
        for message in self.messages:
            self.execute_step(message)

    def execute_step(self, message):
        self.process_message(message)
        time.sleep(10)

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

    def init_messages(self):
        self.messages.append(UserMessage("Ciao, io sono Stefano", {}))
        #self.messages.append(UserMessage("puoi fare la somma fra 9 e 5?", {}))
        self.messages.append(UserMessage("Carica il dataset adult", {}))
        self.messages.append(UserMessage("Pulisci il dataset. Usa il tool clean_dataset", {}))
        #self.messages.append(UserMessage("Puoi disegnare i grafici delle distribuzioni di tutti gli attributi del dataset adult?", {}))
        self.messages.append(UserMessage("Puoi eseguire la codifica del dataset ? Puoi usare il tool esegui_codifica_dataset", {}))
        #self.messages.append(UserMessage("Esegui la trasformazione inversa del dataset.", {}))
        #self.messages.append(UserMessage("Puoi rilevare eventuali variabili proxy presenti nel dataset adult_encoded?", {}))
        #self.messages.append(UserMessage("Dai dati ottenuti puoi dirmi se esistono possibli variabili proxy?", {}))
        #self.messages.append(UserMessage("Puoi disegnare la matrice di correlazione come heatmap del dataset adult_encoded?", {}))
        self.messages.append(UserMessage("Devo predire se il reddito annuo income di un soggetto sara maggiore di 50000 dollari oppure minore od uguale a 50000 dollari. Di quale problema di learning si tratta (classificazione, regressione, clustering.....)? Rispondi nella forma: 'Si tratta di un problema di learning di [tipo_di_problema]'", {}))
        self.messages.append(UserMessage("Quali modelli sono disponibili per risolvere il mio problema di learning? Puoi usare il tool available_models", {}))
        self.messages.append(UserMessage("Quali metriche sono disponibili per il mio problema di learning?", {}))
        self.messages.append(UserMessage("Il dataset è adult e la variabile target è income.", {}))
        self.messages.append(UserMessage("Valuta i modelli usando il dataset adult, variable target income, le metriche disponibili e i modelli disponibili per il mio problema di learning?Usa il tool evaluate_models", {}))
        #self.messages.append(UserMessage("Puoi valutare i modelli [random_forest,gradient_boosting] sul dataset adult e target income?", {}))
        self.messages.append(UserMessage("Da un'analisi delle valutazioni ottenute qual'è,secondo te, il modello più appropriato per predire il reddito annuo income?", {}))
        self.messages.append(UserMessage("Puoi eseguire lo split del dataset in train test set usando come target income? Usa il tool split_dataset_in_train_test_set", {}))
        self.messages.append(UserMessage("Puoi addestrare il modello per te più appropriato fra quelli disponibili e fare una previsione relativa al dataset adult, usando income come target?Usa il tool ", {}))
        #self.messages.append(UserMessage("Puoi addestrare un modello e fare una previsione relativa al dataset adult_encoded?", {}))
        #self.messages.append(UserMessage("Puoi calcolare la distribuzione di tutti gli attributi del dataset adult?", {}))
        #self.messages.append(UserMessage("Noti qualche disproporzione, sbilanciamento negli attributi del dataset adult?", {}))
        #self.messages.append(UserMessage("Puoi calcolare la distribuzione di tutti gli attributi del dataset adult?", {}))
        #self.messages.append(UserMessage("Calcola la matrice di correlazione del dataset adult_encoded", {}))
        #self.messages.append(UserMessage("Noti qualche correlazione importante fra i diversi attributi presenti nella matrice di correlazione del dataset adult?", {}))
        #self.messages.append(UserMessage("Puoi dirmi se esistono disproporzioni, sbilaciamenti, bias negli attributi?", {}))
        #self.messages.append(UserMessage("Non ricordo il mio nome, sai come mi chiamo?", {}))
        #self.messages.append(UserMessage("ricordi se il mio dataset ha l'attributo sex?",{}))
        #self.messages.append(UserMessage("ricordi quali valori può assumere l'attributo sex del mio dataset?", {}))

    def add_memories(self, memories):
        self.add_memory_uc.add_memories(memories)

