from sklearn.feature_selection import mutual_info_classif
import pandas as pd

class MutualInfoUtils:

    @staticmethod
    def get_mutual_info(X, y):
        mi = mutual_info_classif(X, y, random_state=21)
        mi = pd.Series(mi, index=X.columns)
        return mi