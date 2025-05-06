class EncodeDatasetUseCase:

    def __init__(self, dataset_repository, dataset_encoder, dataset_info):
        self.dataset_repository = dataset_repository
        self.dataset_encoder = dataset_encoder
        self.dataset_info = dataset_info

    def encode_dataset(self, dataset_name):
        dataset = self.dataset_repository.get_dataset_by_name(dataset_name)
        encoded_dataset = self.dataset_encoder.encode(dataset, self.dataset_info.get_info())
        #self.dataset_repository.add_dataset(dataset_name + "_encoded", encoded_dataset)
        self.dataset_repository.replace_dataset(dataset_name, encoded_dataset)
        return encoded_dataset

    def decode_dataset(self, dataset_name):
        dataset = self.dataset_repository.get_dataset_by_name(dataset_name)
        decoded_dataset = self.dataset_encoder.decode(dataset)
        self.dataset_repository.replace_dataset(dataset_name, decoded_dataset)
        return decoded_dataset

