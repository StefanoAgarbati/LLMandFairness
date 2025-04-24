class AddMemoryUseCase:

    def __init__(self, memory_repository):
        self.memory_repository = memory_repository

    def add_memory(self, a_memory):
        self.memory_repository.add_memory(a_memory)

    def add_memories(self, memories):
        for memory in memories:
            self.add_memory(memory.get_message())
