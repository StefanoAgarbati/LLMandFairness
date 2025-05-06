from ML.models.models_factory import ModelsFactory


class EvaluateModelUseCase:

    def __init__(self, validator, dataset_repository):
        self.validator = validator
        self.dataset_repository = dataset_repository
        self.cv = 5

    def evaluate_models(self, models, metrics, dataset_name, target):
        models_list = self.get_models_list(models)
        metrics_list = self.get_metrics_list(metrics)
        dataset = self.dataset_repository.get_dataset_by_name(dataset_name)
        results = self.execute_evaluation(models_list, metrics_list, dataset, target)
        return results

    def execute_evaluation(self, models_list, metrics, dataset, target):
        results = []
        for model_name in models_list:
            model = self.create_model(model_name)
            result = self.evaluate_model(model, metrics, dataset, target)
            results.append({"model_name": model.get_model_name(), "score": result})
        return results


    def get_models_list(self, models):
        return models.replace(" ", "").split(",")

    def create_model(self, model_name):
        return ModelsFactory.create_model(model_name)

    def evaluate_model(self, model, metrics, dataset, target):
        result = self.validator.cross_validate_model(model, dataset, target, self.cv, metrics)
        return result

    def get_metrics_list(self, metrics):
        split = metrics.replace(" ", "").split(",")
        return split
