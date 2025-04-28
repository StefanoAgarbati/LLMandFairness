from statis.statistics_support import StatisticsSupport


class CalculateDistributionUseCase:

    def __init__(self, dataset_repository):
        self.dataset_repository = dataset_repository

    def calculate_frequency_distribution(self, dataset_name, attribute_name):
        dataset = self.dataset_repository.get_dataset_by_name(dataset_name)
        #print("CalculateDistributionUseCase calculate_distr() -> dataset type ", type(dataset))
        #print("Attribute name:", attribute_name)
        result = StatisticsSupport.frequency_distribution(dataset[attribute_name])
        #print("calculate_frequency:", result)
        return result

    def calculate_all_frequency_distributions(self, dataset_name):
        dataset = self.dataset_repository.get_dataset_by_name(dataset_name)
        distris = []
        for col_name in dataset.columns:
            distri = dataset[col_name].value_counts().sort_values(ascending=False)
            distris.append(distri)
        return distris


