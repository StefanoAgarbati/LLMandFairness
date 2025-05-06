class UseCaseRepository:

    use_cases = []

    """@staticmethod
    def get_use_case(uc_name):
        match uc_name:
            case UseCase.LOAD_DATASET:
                return UseCaseRepository.load_dataset_use_case
            case UseCase.GET_DISTRIBUTION:
                return UseCaseRepository.get_distribution_use_case"""

    @staticmethod
    def add_use_case(name, use_case):
        #print(f"AddUseCase {name}, {use_case}")
        UseCaseRepository.use_cases.append({"name": name, "use_case": use_case})

    @staticmethod
    def get_use_case_by_name(use_case_name):
        for uc in UseCaseRepository.use_cases:
            if uc['name'] == use_case_name:
                return uc['use_case']
        raise Exception("the use case doesn't exist")

class UseCase:
    GET_AVAILABLE_MODELS = 'available_models'
    DETECT_PROXY = 'detect_proxy'
    DRAW_STATISTICAL_DATA = 'draw_statistical_data'
    DISPLAY = 'display'
    EVALUATE_MODELS = 'evaluate_models'
    FIT_PREDICT_MODEL = 'fit_predict_model'
    SPLIT_TRAIN_TEST = 'split_train_test'
    CLEAN_DATASET = 'clean_dataset'
    ENCODE_DATASET = 'encode_dataset'
    GET_CORRELATION_MATRIX = 'get_correlation_matrix'
    LOAD_DATASET = 'load_dataset'
    GET_DISTRIBUTION = 'get_distribution'