from ML.classification.gradient_boosting_classifier_sklearn import GradientBoostingClassifierSklearn
from ML.classification.random_forest_classifier_sklearn import RandomForestClassifierSklearn


class ClassifierModel:
    RANDOM_FOREST = 'random_forest'
    GRADIENT_BOOSTING = 'gradient_boosting'

class ClassifierFactory:

    @staticmethod
    def create_classifier(classifier_config):
        match classifier_config['model']:
            case ClassifierModel.RANDOM_FOREST:
                return ClassifierFactory.create_random_forest_classifier(classifier_config)
            case ClassifierModel.GRADIENT_BOOSTING:
                return ClassifierFactory.create_gradient_boosting_classifier(classifier_config)

    @staticmethod
    def create_random_forest_classifier(classifier_config):
        return RandomForestClassifierSklearn()

    @staticmethod
    def create_gradient_boosting_classifier(classifier_config):
        return GradientBoostingClassifierSklearn()