from ML.classification.classifier_factory import ClassifierFactory, ClassifierModel


class ModelsFactory:

    @staticmethod
    def create_model(name):
        match name:
            case ClassifierModel.RANDOM_FOREST:
                return ClassifierFactory.create_classifier({"model": name})
            case ClassifierModel.GRADIENT_BOOSTING:
                return ClassifierFactory.create_classifier({"model": name})