from ML.MLProblemType import MLProblemType


class GetAvailableModelsUseCase:

    def __init__(self, models):
        self.models = models

    def get_available_models_for(self, problem_type):
        res = ""
        for model in self.models:
            if model['problem'] == MLProblemType.CLASSIFICATION:
                res += model['name'] + " "

        return res.strip().replace(" ", ", ")
