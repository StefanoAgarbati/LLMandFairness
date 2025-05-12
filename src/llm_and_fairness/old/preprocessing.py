import processingfunctions as fn

class ProcessingData:
    def __init__(self, dataset, values):
        self.dataset = dataset
        self.values = values
    def get_dataset(self):
         return self.dataset
    def get_values(self):
        return self.values

class DatasetPreprocessingConfig:
    def __init__(self, steps, dataset, values_to_replace):
        self.steps = steps
        self.dataset = dataset
        self.values = values_to_replace

    def get_steps(self):
        return self.steps
        
    def get_dataset(self):
        return self.dataset
        
    def get_values(self):
        return self.values

class DatasetPreprocessingBuilder:
    def __init__(self, preprocessing_config):
        self.config = preprocessing_config

    def build(self):
        preprocessing_data = ProcessingData(self.config.get_dataset(), self.config.get_values())
        processor = DatasetPreprocessing(preprocessing_data)
        for step in self.config.get_steps():
            processing_step = ProcessingStepFactory.create_step(step)
            processor.add_step(processing_step)
        return processor
    
        
class DatasetPreprocessing:
    def __init__(self, data):
        self.steps = []
        self.data = data

    def add_step(self, step):
        self.steps.append(step)

    def preprocess_dataset(self):
        processing_data = self.data
        for step in self.steps:
            ds = step.execute(processing_data)
            processing_data = ProcessingData(ds, processing_data.get_values())
        return ds

class ProcessingStepFactory:

    @staticmethod
    def create_step(step_name):
        match step_name:
            case 'remove_whitespaces':
                return RemoveWhitespacesProcessingStep()
            case 'replace_missing_values':
                return ReplaceMissingValuesProcessingStep()
            case 'drop_missing_values':
                handler = DropMissingValuesHandler()
                step = HandleMissingValuesProcessingStep(handler)
                return step
            case _:
                raise Exception("the step name given doesn't exist")
            
class ProcessingStep:
    def execute(self, data):
        pass

class DropMissingValuesHandler:
    def handle(self, data):
        return fn.dropMissingValues(data)

class RemoveWhitespacesProcessingStep(ProcessingStep):
    def execute(self, data):
        return fn.remove_whitespaces(data.get_dataset())
        
class ReplaceMissingValuesProcessingStep(ProcessingStep):
    def execute(self, data):
        return fn.replaceMissingValues(data.get_dataset(), data.get_values())
        
class HandleMissingValuesProcessingStep(ProcessingStep):
    def __init__(self, handler):
        self.handler = handler
        
    def execute(self, data):
        return self.handler.handle(data.get_dataset())
