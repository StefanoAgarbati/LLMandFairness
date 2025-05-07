""""#from src.llm_and_fairness.ML.classification.classifier_factory import ClassifierFactory, ClassifierModel
from ML.classification.classifier_factory import ClassifierFactory, ClassifierModel
from src.llm_and_fairness.ML.encoding.dataset_encoder import DatasetEncoder
from src.llm_and_fairness.ML.prediction_repository import PredictionRepository
from src.llm_and_fairness.ML.split_repository import SplitRepository
from src.llm_and_fairness.ML.validation.cross_validation import CrossValidation
from src.llm_and_fairness.ML.validation.cross_validation_sklearn import CrossValidationSklearn
from src.llm_and_fairness.appl_logic.appl_controller import ApplController
from src.llm_and_fairness.chat.chat_factory import ChatModelType, ChatFactory
from src.llm_and_fairness.datasets.dataset_info import DatasetInfo
from src.llm_and_fairness.datasets.dataset_repository import DatasetRepository
from src.llm_and_fairness.memory.memory_repository import MemoryRepository
from src.llm_and_fairness.messages.user_message import UserMessage
from src.llm_and_fairness.output_device.output_device_factory import OutputDeviceType, OutputDeviceFactory
from src.llm_and_fairness.tools.tool_repository_factory import ToolRepositoryType, ToolRepositoryFactory
from src.llm_and_fairness.tools.tools_functions import clean_dataset
from src.llm_and_fairness.use_cases.add_memory_use_case import AddMemoryUseCase
from src.llm_and_fairness.use_cases.bind_tools_use_case import BindToolsToChatUseCase
from src.llm_and_fairness.use_cases.calculate_distribution_use_case import CalculateDistributionUseCase
from src.llm_and_fairness.use_cases.clean_dataset_use_case import CleanDatasetUseCase
from src.llm_and_fairness.use_cases.encode_dataset_use_case import EncodeDatasetUseCase
from src.llm_and_fairness.use_cases.fit_predict_model_use_case import FitPredictModelUseCase
from src.llm_and_fairness.use_cases.get_correlation_matrix_use_case import GetCorrelationMatrixUseCase
from src.llm_and_fairness.use_cases.get_memories_use_case import GetMemoriesUseCase
from src.llm_and_fairness.use_cases.handle_response_use_case import HandleResponseUseCase
from src.llm_and_fairness.use_cases.load_dataset_use_case import LoadDatasetUseCase
from src.llm_and_fairness.use_cases.model_evaluation_use_case import ModelEvaluationUseCase
from src.llm_and_fairness.use_cases.send_message_use_case import SendMessageUseCase
from src.llm_and_fairness.use_cases.train_test_split_use_case import TrainTestSplitUseCase
from src.llm_and_fairness.use_cases.use_case_repository import UseCaseRepository, UseCase"""
from ML.MLProblemType import MLProblemType
from ML.classification.classifier_factory import ClassifierFactory, ClassifierModel
from ML.classification.classifier_factory import ClassifierFactory, ClassifierModel
from ML.encoding.dataset_encoder import DatasetEncoder
from ML.prediction_repository import PredictionRepository
from ML.split_repository import SplitRepository
from ML.utils.performance_metric_factory import PerformanceMetricsFactory, PerformanceMetric
from ML.utils.proxy_detector import ProxyDetector
from ML.utils.proxy_detector_factory import ProxyDetectorFactory, ProxyDetectorType
from ML.utils.proxy_detector_mutual_info_based import ProxyDetectorMutualInfoBased
from ML.utils.train_test_split_factory import TrainTestSplitFactory, TrainTestSplitType
from ML.validation.cross_validation import CrossValidation
from ML.validation.cross_validation_sklearn import CrossValidationSklearn
from appl_logic.appl_controller import ApplController
from appl_logic.appl_controller_test import ApplControllerTest
from chat.chat_factory import ChatModelType, ChatFactory
from datasets.dataset_info import DatasetInfo
from datasets.dataset_repository import DatasetRepository
from drawing.statistical_drawer_factory import StatisticalDrawerFactory, StatisticalDrawerType
from use_cases.add_memory_use_case import AddMemoryUseCase
from use_cases.bind_tools_use_case import BindToolsToChatUseCase
from use_cases.calculate_distribution_use_case import CalculateDistributionUseCase
from use_cases.clean_dataset_use_case import CleanDatasetUseCase
from use_cases.detect_proxy_use_case import DetectProxyUseCase
from use_cases.display_use_case import DisplayUseCase
from use_cases.draw_statistical_data import DrawStatisticalDataUseCase
from use_cases.encode_dataset_use_case import EncodeDatasetUseCase
from use_cases.evaluate_model_use_case import EvaluateModelUseCase
from use_cases.fit_predict_model_use_case import FitPredictModelUseCase
from use_cases.get_available_metrics_use_case import GetAvailableMetricsUseCase
from use_cases.get_available_models_use_case import GetAvailableModelsUseCase, GetAvailableModelsUseCase
from use_cases.get_correlation_matrix_use_case import GetCorrelationMatrixUseCase
from use_cases.get_memories_use_case import GetMemoriesUseCase
from use_cases.handle_response_use_case import HandleResponseUseCase
from use_cases.load_dataset_use_case import LoadDatasetUseCase
from use_cases.model_evaluation_use_case import ModelEvaluationUseCase
from use_cases.send_message_use_case import SendMessageUseCase
from use_cases.train_model_and_make_prediction import TrainModelAndMakePrediction
from use_cases.train_test_split_use_case import TrainTestSplitUseCase
from use_cases.use_case_repository import UseCaseRepository, UseCase
from memory.memory_repository import MemoryRepository
from messages.user_message import UserMessage
from output_device.output_device_factory import OutputDeviceType, OutputDeviceFactory
from tools.tool_repository_factory import ToolRepositoryType, ToolRepositoryFactory
from tools.tools_functions import clean_dataset


class SystemConfig:
    chat_type = ChatModelType.GOOGLE
    model_name = 'gemini-2.0-flash'
    api_key = 'AIzaSyCNfAQnkwlkPZbE_CTIn-GSQPks-fmQMkY'
    out_dev_type = OutputDeviceType.Jupyter
    tool_repo_type = ToolRepositoryType.LANGCHAIN
    dataset_name = 'adult'
    classifier_config = {"model": ClassifierModel.GRADIENT_BOOSTING}
    scorings = ['accuracy', 'precision', 'recall', 'f1']
    models = [ClassifierModel.RANDOM_FOREST, ClassifierModel.GRADIENT_BOOSTING]
    drawer = StatisticalDrawerType.SEABORN
    splitter = TrainTestSplitType.SKLEARN
    performance_metrics = PerformanceMetric.SKLEARN
    proxy_detector_config = {"type": ProxyDetectorType.MutualInfo, "metrics": performance_metrics}
    available_models = [{"name":ClassifierModel.RANDOM_FOREST, "problem": "classificazione"},
                        {"name": ClassifierModel.GRADIENT_BOOSTING, "problem": "classificazione"}]
    available_metrics = [{"problem": MLProblemType.CLASSIFICATION, "metrics": "accuracy, precision, recall, f1"}]

def create_test_msg():
    msg = "Carica il dataset {dataset}"
    params = {
        "dataset": "adult"
    }
    return UserMessage(msg, params)


def create_chat(ctype, model_name, api_key):
    chat = ChatFactory.create_chat(ctype, model_name, api_key)
    return chat


def create_send_message_use_case(achat):
    uc = SendMessageUseCase(achat)
    return uc


def create_bind_tools_use_case(tool_repository, achat):
    return BindToolsToChatUseCase(tool_repository, achat)


def create_load_dataset_use_case(dataset_repository):
    #print("create_load_dataset_use_case")
    return LoadDatasetUseCase(dataset_repository)


def create_calculate_distr_use_case(dataset_repository):
    return CalculateDistributionUseCase(dataset_repository)


def create_dataset_repository():
    return DatasetRepository()


def create_tool_repository(repo_type):
    repo = ToolRepositoryFactory.create(repo_type)
    return repo


def create_response_handler(tool_repository):
    return HandleResponseUseCase(tool_repository)


def create_output_device(out_device_type):
    return OutputDeviceFactory.createOutputDevice(out_device_type)


def create_memory_repository():
    return MemoryRepository()


def create_add_memory_use_case(memory_repository):
    return AddMemoryUseCase(memory_repository)


def create_get_memories_use_case(memory_repository):
    return GetMemoriesUseCase(memory_repository)


def create_get_correlation_matrix_use_case(dataset_repository):
    return GetCorrelationMatrixUseCase(dataset_repository)


def create_clean_dataset_use_case(dataset_repository):
    return CleanDatasetUseCase(dataset_repository)


def create_train_test_split_use_case(split_repository, dataset_repository, splitter):
    return TrainTestSplitUseCase(split_repository, dataset_repository, splitter)


def create_split_repository():
    return SplitRepository()


def create_fit_predict_model_use_case(classifier, split_repository, prediction_repository):
    return FitPredictModelUseCase(classifier, split_repository, prediction_repository)


def create_classifier(classifier_config):
    return ClassifierFactory.create_classifier(classifier_config)


def create_models(models_names):
    models = []
    for name in models_names:
        model = ClassifierFactory.create_classifier({"model": name})
        models.append(model)
    return models


def create_prediction_repository():
    return PredictionRepository()


def create_encode_dataset_use_case(dataset_repository, dataset_encode, dataset_info):
    return EncodeDatasetUseCase(dataset_repository, dataset_encode, dataset_info)


def create_dataset_encoder():
    return DatasetEncoder()


def create_dataset_info(dataset_name):
    return DatasetInfo.create(dataset_name)


def create_evaluate_models_use_case(validator, models, scorings, dataset_repository):
    return ModelEvaluationUseCase(validator, models, scorings, dataset_repository)

def create_models_evaluation_use_case(validator, dataset_repository):
    return EvaluateModelUseCase(validator, dataset_repository)

def create_cross_validator():
    return CrossValidationSklearn()


def create_display_use_case(output_device):
    return DisplayUseCase(output_device)


def create_draw_statistical_data_use_case(dataset_repository, drawer, get_correlation_matrix_uc):
    return DrawStatisticalDataUseCase(dataset_repository, drawer, get_correlation_matrix_uc)


def create_drawer(name):
    return StatisticalDrawerFactory.create_statistical_drawer(name)

def create_detect_proxy_use_case(dataset_repository, proxy_detector):
    return DetectProxyUseCase(dataset_repository, proxy_detector)



def create_proxy_detector(config):
    return ProxyDetectorFactory.create(config)

def create_splitter(type):
    return TrainTestSplitFactory.create_train_test_splitter(type)

def create_performance_metrics(type):
    return PerformanceMetricsFactory.create_performance_metrics(type)

def create_get_available_models_use_case(available_models):
    return GetAvailableModelsUseCase(available_models)

def create_get_available_metrics_use_case(metrics):
    return GetAvailableMetricsUseCase(metrics)

def create_train_model_and_make_prediction_use_case(split_repository, prediction_repository):
    return TrainModelAndMakePrediction(split_repository, prediction_repository)

def create_system():
    chat = create_chat(SystemConfig.chat_type, SystemConfig.model_name, SystemConfig.api_key)
    output_device = create_output_device(SystemConfig.out_dev_type)
    dataset_repository = create_dataset_repository()
    load_dataset_uc = create_load_dataset_use_case(dataset_repository)
    calculate_distr_uc = create_calculate_distr_use_case(dataset_repository)
    tool_repository = create_tool_repository(SystemConfig.tool_repo_type)
    response_handler = create_response_handler(tool_repository)
    memory_repository = create_memory_repository()
    add_memory_uc = create_add_memory_use_case(memory_repository)
    get_memories_uc = create_get_memories_use_case(memory_repository)
    get_correlation_matrix_uc = create_get_correlation_matrix_use_case(dataset_repository)
    dataset_info = create_dataset_info(SystemConfig.dataset_name)
    dataset_encoder = create_dataset_encoder()
    validator = create_cross_validator()
    models = create_models(SystemConfig.models)
    encode_dataset_uc = create_encode_dataset_use_case(dataset_repository, dataset_encoder, dataset_info)
    clean_dataset_uc = create_clean_dataset_use_case(dataset_repository)
    split_repository = create_split_repository()
    splitter = create_splitter(SystemConfig.splitter)
    train_test_split_uc = create_train_test_split_use_case(split_repository, dataset_repository, splitter)
    prediction_repository = create_prediction_repository()
    classifier = create_classifier(SystemConfig.classifier_config)
    fit_predict_uc = create_fit_predict_model_use_case(classifier, split_repository, prediction_repository)
    evaluate_models_uc = create_evaluate_models_use_case(validator, models, SystemConfig.scorings, dataset_repository)
    display_uc = create_display_use_case(output_device)
    drawer = create_drawer(SystemConfig.drawer)
    draw_statistical_data_use_case = create_draw_statistical_data_use_case(dataset_repository, drawer,
                                                                           get_correlation_matrix_uc)
    performance_metrics = create_performance_metrics(SystemConfig.performance_metrics)
    #splitter = create_splitter(SystemConfig.splitter)
    proxy_detector = create_proxy_detector(SystemConfig.proxy_detector_config)
    proxy_detector_uc = create_detect_proxy_use_case(dataset_repository, proxy_detector)
    get_available_models_use_case = create_get_available_models_use_case(SystemConfig.available_models)
    models_evaluation_uc = create_models_evaluation_use_case(validator, dataset_repository)
    get_available_metrics_uc = create_get_available_metrics_use_case(SystemConfig.available_metrics)
    train_model_and_make_prediction_uc = create_train_model_and_make_prediction_use_case(split_repository, prediction_repository)

    UseCaseRepository.add_use_case(UseCase.DETECT_PROXY, proxy_detector_uc)
    UseCaseRepository.add_use_case(UseCase.LOAD_DATASET, load_dataset_uc)
    UseCaseRepository.add_use_case(UseCase.GET_DISTRIBUTION, calculate_distr_uc)
    UseCaseRepository.add_use_case(UseCase.GET_CORRELATION_MATRIX, get_correlation_matrix_uc)
    UseCaseRepository.add_use_case(UseCase.ENCODE_DATASET, encode_dataset_uc)
    UseCaseRepository.add_use_case(UseCase.CLEAN_DATASET, clean_dataset_uc)
    UseCaseRepository.add_use_case(UseCase.SPLIT_TRAIN_TEST, train_test_split_uc)
    UseCaseRepository.add_use_case(UseCase.FIT_PREDICT_MODEL, fit_predict_uc)
    UseCaseRepository.add_use_case(UseCase.EVALUATE_MODELS, evaluate_models_uc)
    UseCaseRepository.add_use_case(UseCase.DISPLAY, display_uc)
    UseCaseRepository.add_use_case(UseCase.DRAW_STATISTICAL_DATA, draw_statistical_data_use_case)
    UseCaseRepository.add_use_case(UseCase.GET_AVAILABLE_MODELS, get_available_models_use_case)
    UseCaseRepository.add_use_case(UseCase.MODELS_EVALUATION, models_evaluation_uc)
    UseCaseRepository.add_use_case(UseCase.GET_AVAILABLE_METRICS, get_available_metrics_uc)
    UseCaseRepository.add_use_case(UseCase.TRAIN_MODEL_MAKE_PREDICTION, train_model_and_make_prediction_uc)

    send_msg_uc = create_send_message_use_case(chat)
    bind_tools_uc = create_bind_tools_use_case(tool_repository, chat)

    bind_tools_uc.bind_tools()

    appl_logic = ApplControllerTest(add_memory_uc, get_memories_uc, display_uc, response_handler, send_msg_uc)
    appl_logic.execute()


create_system()
