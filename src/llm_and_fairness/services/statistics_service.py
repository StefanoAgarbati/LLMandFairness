from src.llm_and_fairness.statis.statistics_support import StatisticsSupport


class StatisticsService:

    def frequency_distribution(self, data):
        return StatisticsSupport.frequency_distribution(data)

    def relative_frequency_distribution(self, data):
        return StatisticsSupport.relative_frequency_distribution(data)

    def percentage_distribution(self, data):
        return StatisticsSupport.percentage_distribution(data)