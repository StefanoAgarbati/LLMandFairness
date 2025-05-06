class GetAvailableModelsUseCase:

    def __init__(self, models):
        self.models = models

    def get_available_models_for(self, problem_type):
        res = ""
        for model in self.models:
            if model['problem'] == 'classificazione':
                res += model['name'] + " "

        return res.strip().replace(" ", ", ")
