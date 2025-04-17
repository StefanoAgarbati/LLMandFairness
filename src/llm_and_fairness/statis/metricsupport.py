from statis.statisdomain import Distribution, StatisticsSupport

def frequency_distribution(data):
    distribution = data.value_counts().sort_index()
    return distribution

def relative_frequency_distribution(data):
    n = data.size
    distribution = frequency_distribution(data)
    relative = distribution / n
    return relative

def percentage_distribution(data):
    return relative_frequency_distribution(data) * 100

class StatisticsSupportImpl(StatisticsSupport):
    def __init__(self, dataset):
        self.dataset = dataset
    
    def get_distribution(self, attribute_name, distribution_type):
        print("get_distribution called")
        data = None
        if distribution_type == 'frequency':
            data = frequency_distribution(self.dataset[attribute_name])
        elif distribution_type == 'relative':
            data = relative_frequency_distribution(self.dataset[attribute_name])
        elif distribution_type == 'percentage':
            data = percentage_distribution(self.dataset[attribute_name])
        distr = Distribution(attribute_name, data.to_dict())
        return distr