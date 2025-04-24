class UseCaseRepository:

    load_dataset_use_case = None
    get_distribution_use_case = None
    use_cases = []

    @staticmethod
    def get_use_case(uc_name):
        match uc_name:
            case UseCase.LOAD_DATASET:
                return UseCaseRepository.load_dataset_use_case
            case UseCase.GET_DISTRIBUTION:
                return UseCaseRepository.get_distribution_use_case

    @staticmethod
    def add_use_case(name, use_case):
        UseCaseRepository.use_cases.append({"name": name, "use_case": use_case})

    @staticmethod
    def get_use_case_by_name(use_case_name):
        for uc in UseCaseRepository.use_cases:
            if uc['name'] == use_case_name:
                return uc['use_case']
        raise Exception("the use case doesn't exist")

class UseCase:
    LOAD_DATASET = 'load_dataset'
    GET_DISTRIBUTION = 'get_distribution'