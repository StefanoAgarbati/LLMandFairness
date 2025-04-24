class MemoryRepository:

    def __init__(self):
        self.memory = []

    def add_memory(self, a_memory):
        self.memory.append(a_memory)

    def get_memories(self):
        return self.memory