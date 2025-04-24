from src.llm_and_fairness.support import DatasetFactory


class DatasetService:

    def __init__(self, dataset_repository):
        self.dataset_repository = dataset_repository

    def load_dataset(self, name):
        has_dataset = self.dataset_repository.has_dataset(name)
        if has_dataset:
            return
        dataset = DatasetFactory.create_dataset(name)
        self.dataset_repository.add_dataset(name, dataset)
