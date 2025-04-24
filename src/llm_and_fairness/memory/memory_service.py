from src.llm_and_fairness.memory.memory import Memory


class MemoryService:

    def __init__(self, memory_repository):
        self.memory_repository = memory_repository

    def add_memory(self, a_memory_string: str) -> None:
        a_memory = Memory(a_memory_string)
        self.memory_repository.add_memory(a_memory)

    def get_memories(self) -> list[Memory]:
        return self.memory_repository.get_memories()