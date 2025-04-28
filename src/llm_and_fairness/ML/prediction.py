class Prediction:
    def __init__(self, name, y_pred):
        self.name = name
        self.pred = y_pred

    def get_name(self):
        return self.name

    def get_y_pred(self):
        return self.pred


