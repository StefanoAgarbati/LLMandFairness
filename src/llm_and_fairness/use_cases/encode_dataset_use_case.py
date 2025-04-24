class EncodeDatasetUseCase:

    def __init__(self, dataset_repository, dataset_encoder, dataset_info):
        self.dataset_repository = dataset_repository
        self.dataset_encoder = dataset_encoder
        self.dataset_info = dataset_info

    def encode_dataset(self, dataset_name, encoding_config):
        dataset = self.dataset_repository.get_dataset_by_name(dataset_name)
        encoded_dataset = self.dataset_encoder(dataset, self.dataset_info)
        return encoded_dataset


