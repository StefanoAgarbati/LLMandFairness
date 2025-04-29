import json

from cleaning.preprocessing import DatasetPreprocessingConfig, DatasetPreprocessingBuilder


class DatasetCleaner:

    config_path = "cleaning/preprocessingconfig.json"

    def __init__(self, dataset):
        self.dataset = dataset
        self.processor = self.init_processor()

    def clean_dataset(self):
        return self.processor.preprocess_dataset()

    def init_processor(self):
        config = self.create_config()
        builder = self.create_builder(config)
        processor = self.create_processor(builder)
        return processor

    def create_config(self):
        json_obj = json.load(open(DatasetCleaner.config_path, "r"))
        steps = json_obj['steps']
        values_to_replace = json_obj['values_to_replace']
        config = DatasetPreprocessingConfig(steps, self.dataset, values_to_replace)
        return config

    def create_builder(self, config):
        builder = DatasetPreprocessingBuilder(config)
        return builder

    def create_processor(self, builder):
        return builder.build()