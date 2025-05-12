from ML.MLProblemType import MLProblemType
from ML.classification.classifier_factory import ClassifierModel
from ML.utils.performance_metric_factory import PerformanceMetric
from ML.utils.proxy_detector_factory import ProxyDetectorType
from ML.utils.train_test_split_factory import TrainTestSplitType
from chat.chat_factory import ChatModelType
from drawing.statistical_drawer_factory import StatisticalDrawerType
from output_device.output_device_factory import OutputDeviceType
from tools.tool_repository_factory import ToolRepositoryType


class SystemConfig:
    chat_type = ChatModelType.GOOGLE
    model_name = 'gemini-2.0-flash'
    api_key = 'AIzaSyCNfAQnkwlkPZbE_CTIn-GSQPks-fmQMkY'
    out_dev_type = OutputDeviceType.Jupyter
    tool_repo_type = ToolRepositoryType.STANDARD
    dataset_name = 'bank'
    cleaning_config_path = 'datasets/bank/preprocessingconfig.json'
    user_message_path = 'datasets/bank/message_template.json'
    classifier_config = {"model": ClassifierModel.GRADIENT_BOOSTING}
    scorings = ['accuracy', 'precision', 'recall', 'f1']
    models = [ClassifierModel.RANDOM_FOREST, ClassifierModel.GRADIENT_BOOSTING]
    drawer = StatisticalDrawerType.SEABORN
    splitter = TrainTestSplitType.SKLEARN
    performance_metrics = PerformanceMetric.SKLEARN
    proxy_detector_config = {"type": ProxyDetectorType.MutualInfo, "metrics": performance_metrics}
    available_models = [{"name": ClassifierModel.RANDOM_FOREST, "problem": "classificazione"},
                        {"name": ClassifierModel.GRADIENT_BOOSTING, "problem": "classificazione"}]
    available_metrics = [{"problem": MLProblemType.CLASSIFICATION, "metrics": "accuracy, precision, recall, f1"}]
    fairness_available_metrics = [{"problem": MLProblemType.CLASSIFICATION,
                                   "disaggregated_metrics": "accuracy, selection_rate",
                                   "aggregated_metrics": "demographic_parity_difference, demographic_parity_ratio"}]
    fairness_metrics_name = 'fairlearn'