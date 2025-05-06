from ML.encoding.encoder_factory import EncoderFactory, EncoderType


class DatasetEncoder:

    def __init__(self):
        self.encoders_map = []

    def encode(self, dataset, dataset_info):
        self.encoders_map = self.get_encoders_map(dataset_info)
        encoded_dataset = self.encode_dataset(dataset, self.encoders_map)
        return encoded_dataset

    def decode(self, dataset):
        ds = dataset.copy()
        for encoder in self.encoders_map:
            attribute_name = encoder['name']
            ds[attribute_name] = self.decode_attribute(ds, attribute_name)
        return ds

    def decode_attribute(self, dataset, attribute_name):
        column_to_decode = dataset[attribute_name]
        column_decoded = self.decode_column(column_to_decode, attribute_name)
        return column_decoded

    def decode_column(self, column, attribute_name):
        encoder_for_column = self.get_encoder_for_attribute(attribute_name)
        column_decoded = encoder_for_column.decode(column)
        return column_decoded

    def get_encoder_for_attribute(self, attribute_name):
        for encoder in self.encoders_map:
            if encoder['name'] == attribute_name:
                return encoder
        raise Exception(f"The encoder for {attribute_name} doesn't exist")

    def get_encoders_map(self, dataset_info):
        encoders_map = []
        for info in dataset_info:
            attribute_name = info['name']
            attribute_type = info['type']
            categories = None
            if attribute_type == EncoderType.ORDINAL_ENCODER:
                categories = info['values']
            encoder = EncoderFactory.create_encoder(attribute_type, categories)
            encoders_map.append({"name": attribute_name, "encoder": encoder})
        return encoders_map

    def encode_dataset(self, dataset, encoders_map):
        ds = dataset.copy()
        for item in encoders_map:
            attribute_name = item['name']
            encoder = item['encoder']
            ds = self.encode_attribute(ds, attribute_name, encoder)
        return ds

    def encode_attribute(self, dataset, attribute_name, encoder):
        dataset[attribute_name] = encoder.encode(dataset[[attribute_name]])
        return dataset


