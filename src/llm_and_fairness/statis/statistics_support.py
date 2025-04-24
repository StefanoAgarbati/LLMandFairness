class StatisticsSupport:

    @staticmethod
    def frequency_distribution(data):
        #print(f"StatisticsSupport frequency_distribution()")
        distribution = data.value_counts().sort_index()
        #print(f"StatisticsSupport frequency_distribution() -> {distribution}")
        return distribution

    @staticmethod
    def relative_frequency_distribution(data):
        n = data.size
        distribution = StatisticsSupport.frequency_distribution(data)
        relative = distribution / n
        return relative

    @staticmethod
    def percentage_distribution(data):
        return StatisticsSupport.relative_frequency_distribution(data) * 100