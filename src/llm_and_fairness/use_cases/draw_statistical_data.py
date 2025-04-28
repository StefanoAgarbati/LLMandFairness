class DrawStatisticalDataUseCase:
    
    def __init__(self, dataset_repository, drawer, get_correlation_matrix_uc):
        self.dataset_repository = dataset_repository
        self.drawer = drawer
        self.get_correlation_matrix_uc = get_correlation_matrix_uc

    def draw_correlation_matrix(self, dataset_name):
        correlation_matrix = self.get_correlation_matrix_uc.get_correlation_matrix(dataset_name)
        figure = self.drawer.heatmap(correlation_matrix, figsize=(10, 6), fmt='.2f', colormap='coolwarm')
        return figure

    def draw_all_distributions(self, dataset_name):
        dataset = self.dataset_repository.get_dataset_by_name(dataset_name)
        figures = []
        for column in dataset.columns:
            figure = self.do_draw_distribution(dataset, column)
            figures.append(figure)
        return figures

    def draw_distribution(self, dataset_name, attribute_name):
        dataset = self.dataset_repository.get_dataset_by_name(dataset_name)
        return self.do_draw_distribution(dataset, attribute_name)

    def do_draw_distribution(self, dataset, attribute_name):
        if self.is_categorical(dataset, attribute_name):
            return self.draw_categorical(dataset, attribute_name)
        if self.is_numeric(dataset, attribute_name):
            return self.draw_numeric(dataset, attribute_name)

    def draw_numeric(self, dataset, attribute_name):
        return self.drawer.histplot(dataset, attribute_name)

    def draw_categorical(self, dataset, attribute_name):
        return self.drawer.countplot(dataset, attribute_name)

    def is_categorical(self, dataset, attribute_name):
        col = dataset[attribute_name]
        is_cat = isinstance(col[0], str)
        return is_cat

    def is_numeric(self, dataset, attribute_name):
        return not self.is_categorical(dataset, attribute_name)