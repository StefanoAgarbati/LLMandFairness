class GetMemoriesUseCase:

    def __init__(self, memory_repository):
        self.repo = memory_repository

    def get_memories(self):
        return self.repo.get_memories()

