from cleaning.dataset_cleaner import DatasetCleaner


class CleanDatasetUseCase:

    def __init__(self, dataset_repository, clean_config_path):
        self.dataset_repository = dataset_repository
        self.clean_config = clean_config_path

    def clean_dataset(self, dataset_name):
        dataset = self.dataset_repository.get_dataset_by_name(dataset_name)
        #print("CleanDatasetUseCase dataset:", dataset)
        cleaner = DatasetCleaner(dataset, self.clean_config)
        cleaned_dataset = cleaner.clean_dataset()
        self.dataset_repository.replace_dataset(dataset_name, cleaned_dataset)
        return cleaned_dataset
