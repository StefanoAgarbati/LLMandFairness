class ModelEvaluationUseCase:

    def __init__(self, validator, models, scorings, dataset_repository):
        self.validator = validator
        self.models = models
        self.scorings = scorings
        self.cv = 5
        self.dataset_repository = dataset_repository

    def evaluate_models(self, dataset_name, target):
        scores = []
        dataset = self.dataset_repository.get_dataset_by_name(dataset_name)
        for model in self.models:
            score = self.validator.cross_validate_model(model, dataset, target, self.cv, self.scorings)
            scores.append({"model_name": model.get_model_name(), "score": score})
        return scores
