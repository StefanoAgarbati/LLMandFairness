from src.llm_and_fairness.statis.statistics_support import StatisticsSupport


class GetCorrelationMatrixUseCase:

    def __init__(self, dataset_repository):
        self.dataset_repository = dataset_repository

    def get_correlation_matrix(self, dataset_name):
        dataset = self.dataset_repository.get_dataset_by_name(dataset_name)
        result = StatisticsSupport.correlation_matrix(dataset)
        return result
