import pandas as pd

from ML.validation.cross_validation import CrossValidation
import sklearn.model_selection as ms

class CrossValidationSklearn(CrossValidation):

    def cross_validate_model(self, model, dataset, target, cv, scorings):
        X = dataset.drop(columns=target)
        y = dataset[target]
        results = ms.cross_validate(model.get_model(), X, y, cv=cv, scoring=scorings)
        df_results = pd.DataFrame(results)
        return df_results
