class PredictionRepository:

    def __init__(self):
        self.predictions = []

    def add_prediction(self, prediction):
        self.predictions.append(prediction)

    def get_prediction_by_name(self, name):
        for prediction in self.predictions:
            if prediction.get_name() == name:
                return prediction
        raise Exception(f"The prediction {name} doesn't exist")
