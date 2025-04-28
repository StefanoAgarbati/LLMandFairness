from ML.encoding.encoder_factory import EncoderFactory, EncoderType


class DatasetEncoder:

    def encode(self, dataset, dataset_info):
        encoders_map = self.get_encoders_map(dataset_info)
        encoded_dataset = self.encode_dataset(dataset, encoders_map)
        return encoded_dataset

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
            ds = self.encode_attribute(dataset, attribute_name, encoder)
        return ds

    def encode_attribute(self, dataset, attribute_name, encoder):
        dataset[attribute_name] = encoder.encode(dataset[[attribute_name]])
        return dataset


