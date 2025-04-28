from cleaning.dataset_cleaner import DatasetCleaner


class CleanDatasetUseCase:

    def __init__(self, dataset_repository):
        self.dataset_repository = dataset_repository

    def clean_dataset(self, dataset_name):
        dataset = self.dataset_repository.get_dataset_by_name(dataset_name)
        #print("CleanDatasetUseCase dataset:", dataset)
        cleaner = DatasetCleaner(dataset)
        cleaned_dataset = cleaner.clean_dataset()
        self.dataset_repository.replace_dataset(dataset_name, cleaned_dataset)
        return cleaned_dataset
