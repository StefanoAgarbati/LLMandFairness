from ML.classification.classifier_factory import ClassifierFactory
from ML.encoding.dataset_encoder import DatasetEncoder
from ML.prediction_repository import PredictionRepository
from ML.split_repository import SplitRepository
from ML.utils.performance_metric_factory import PerformanceMetricsFactory
from ML.utils.proxy_detector_factory import ProxyDetectorFactory
from ML.utils.train_test_split_factory import TrainTestSplitFactory
from ML.validation.cross_validation_sklearn import CrossValidationSklearn
from appl_logic.appl_controller import ApplController
from chat.chat_factory import ChatFactory
from datasets.dataset_info import DatasetInfo
from datasets.dataset_repository import DatasetRepository
from drawing.statistical_drawer_factory import StatisticalDrawerFactory
from messages.user_message_repository_factory import UserMessageRepositoryFactory
from use_cases.add_memory_use_case import AddMemoryUseCase
from use_cases.bind_tools_use_case import BindToolsToChatUseCase
from use_cases.calculate_distribution_use_case import CalculateDistributionUseCase
from use_cases.clean_dataset_use_case import CleanDatasetUseCase
from use_cases.detect_proxy_use_case import DetectProxyUseCase
from use_cases.display_use_case import DisplayUseCase
from use_cases.draw_statistical_data import DrawStatisticalDataUseCase
from use_cases.encode_dataset_use_case import EncodeDatasetUseCase
from use_cases.fit_predict_model_use_case import FitPredictModelUseCase
from use_cases.get_correlation_matrix_use_case import GetCorrelationMatrixUseCase
from use_cases.get_memories_use_case import GetMemoriesUseCase
from use_cases.get_user_messages_use_case import GetUserMessagesUseCase
from use_cases.handle_response_use_case import HandleResponseUseCase
from use_cases.load_dataset_use_case import LoadDatasetUseCase
from use_cases.model_evaluation_use_case import ModelEvaluationUseCase
from use_cases.send_message_use_case import SendMessageUseCase
from use_cases.train_test_split_use_case import TrainTestSplitUseCase
from use_cases.use_case_repository import UseCaseRepository, UseCase
from memory.memory_repository import MemoryRepository
from output_device.output_device_factory import OutputDeviceFactory
from tools.tool_repository_factory import ToolRepositoryFactory
from system_config import SystemConfig


class MainLLMAndFairness:

    def __init__(self):
        self.create_system()
        self.start_the_system()

    def create_chat(self, ctype, model_name, api_key):
        chat = ChatFactory.create_chat(ctype, model_name, api_key)
        return chat


    def create_send_message_use_case(self, achat):
        uc = SendMessageUseCase(achat)
        return uc


    def create_bind_tools_use_case(self, tool_repository, achat):
        return BindToolsToChatUseCase(tool_repository, achat)


    def create_load_dataset_use_case(self, dataset_repository):
        # print("create_load_dataset_use_case")
        return LoadDatasetUseCase(dataset_repository)


    def create_calculate_distr_use_case(self, dataset_repository):
        return CalculateDistributionUseCase(dataset_repository)


    def create_dataset_repository(self):
        return DatasetRepository()


    def create_tool_repository(self, repo_type):
        repo = ToolRepositoryFactory.create(repo_type)
        return repo


    def create_response_handler(self, tool_repository):
        return HandleResponseUseCase(tool_repository)


    def create_output_device(self, out_device_type):
        return OutputDeviceFactory.createOutputDevice(out_device_type)


    def create_memory_repository(self):
        return MemoryRepository()


    def create_add_memory_use_case(self, memory_repository):
        return AddMemoryUseCase(memory_repository)


    def create_get_memories_use_case(self, memory_repository):
        return GetMemoriesUseCase(memory_repository)


    def create_get_correlation_matrix_use_case(self, dataset_repository):
        return GetCorrelationMatrixUseCase(dataset_repository)


    def create_clean_dataset_use_case(self, dataset_repository):
        return CleanDatasetUseCase(dataset_repository)


    def create_train_test_split_use_case(self, split_repository, dataset_repository, splitter):
        return TrainTestSplitUseCase(split_repository, dataset_repository, splitter)


    def create_split_repository(self):
        return SplitRepository()


    def create_fit_predict_model_use_case(self, classifier, split_repository, prediction_repository):
        return FitPredictModelUseCase(classifier, split_repository, prediction_repository)


    def create_classifier(self, classifier_config):
        return ClassifierFactory.create_classifier(classifier_config)


    def create_models(self, models_names):
        models = []
        for name in models_names:
            model = ClassifierFactory.create_classifier({"model": name})
            models.append(model)
        return models


    def create_prediction_repository(self):
        return PredictionRepository()


    def create_encode_dataset_use_case(self, dataset_repository, dataset_encode, dataset_info):
        return EncodeDatasetUseCase(dataset_repository, dataset_encode, dataset_info)


    def create_dataset_encoder(self):
        return DatasetEncoder()


    def create_dataset_info(self, dataset_name):
        return DatasetInfo.create(dataset_name)


    def create_evaluate_models_use_case(self, validator, models, scorings, dataset_repository):
        return ModelEvaluationUseCase(validator, models, scorings, dataset_repository)


    def create_cross_validator(self):
        return CrossValidationSklearn()


    def create_display_use_case(self, output_device):
        return DisplayUseCase(output_device)


    def create_draw_statistical_data_use_case(self, dataset_repository, drawer, get_correlation_matrix_uc):
        return DrawStatisticalDataUseCase(dataset_repository, drawer, get_correlation_matrix_uc)


    def create_drawer(self, name):
        return StatisticalDrawerFactory.create_statistical_drawer(name)


    def create_detect_proxy_use_case(self, dataset_repository, proxy_detector):
        return DetectProxyUseCase(dataset_repository, proxy_detector)


    def create_proxy_detector(self, config):
        return ProxyDetectorFactory.create(config)


    def create_splitter(self, type):
        return TrainTestSplitFactory.create_train_test_splitter(type)


    def create_performance_metrics(self, type):
        return PerformanceMetricsFactory.create_performance_metrics(type)

    def create_get_user_message_use_case(self, user_message_repository):
        return GetUserMessagesUseCase(user_message_repository)

    def create_user_message_repository(self):
        return UserMessageRepositoryFactory.createUserMessageRepository()

    def create_system(self):
        self.chat = self.create_chat(SystemConfig.chat_type, SystemConfig.model_name, SystemConfig.api_key)
        self.output_device = self.create_output_device(SystemConfig.out_dev_type)
        self.dataset_repository = self.create_dataset_repository()
        self.load_dataset_uc = self.create_load_dataset_use_case(self.dataset_repository)
        self.calculate_distr_uc = self.create_calculate_distr_use_case(self.dataset_repository)
        self.tool_repository = self.create_tool_repository(SystemConfig.tool_repo_type)
        self.response_handler = self.create_response_handler(self.tool_repository)
        self.memory_repository = self.create_memory_repository()
        self.add_memory_uc = self.create_add_memory_use_case(self.memory_repository)
        self.get_memories_uc = self.create_get_memories_use_case(self.memory_repository)
        self.get_correlation_matrix_uc = self.create_get_correlation_matrix_use_case(self.dataset_repository)
        self.dataset_info = self.create_dataset_info(SystemConfig.dataset_name)
        self.dataset_encoder = self.create_dataset_encoder()
        self.validator = self.create_cross_validator()
        self.models = self.create_models(SystemConfig.models)
        self.encode_dataset_uc = self.create_encode_dataset_use_case(self.dataset_repository, self.dataset_encoder, self.dataset_info)
        self.clean_dataset_uc = self.create_clean_dataset_use_case(self.dataset_repository)
        self.split_repository = self.create_split_repository()
        self.splitter = self.create_splitter(SystemConfig.splitter)
        self.train_test_split_uc = self.create_train_test_split_use_case(self.split_repository, self.dataset_repository, self.splitter)
        self.prediction_repository = self.create_prediction_repository()
        self.classifier = self.create_classifier(SystemConfig.classifier_config)
        self.fit_predict_uc = self.create_fit_predict_model_use_case(self.classifier, self.split_repository, self.prediction_repository)
        self.evaluate_models_uc = self.create_evaluate_models_use_case(self.validator, self.models, SystemConfig.scorings, self.dataset_repository)
        self.display_uc = self.create_display_use_case(self.output_device)
        self.drawer = self.create_drawer(SystemConfig.drawer)
        self.draw_statistical_data_use_case = self.create_draw_statistical_data_use_case(self.dataset_repository, self.drawer,
                                                                           self.get_correlation_matrix_uc)
        self.performance_metrics = self.create_performance_metrics(SystemConfig.performance_metrics)
        # self.splitter = self.create_splitter(SystemConfig.splitter)
        self.proxy_detector = self.create_proxy_detector(SystemConfig.proxy_detector_config)
        self.proxy_detector_uc = self.create_detect_proxy_use_case(self.dataset_repository, self.proxy_detector)
        self.user_message_repository = self.create_user_message_repository()
        self.get_user_message_uc = self.create_get_user_message_use_case(self.user_message_repository)


        UseCaseRepository.add_use_case(UseCase.DETECT_PROXY, self.proxy_detector_uc)
        UseCaseRepository.add_use_case(UseCase.LOAD_DATASET, self.load_dataset_uc)
        UseCaseRepository.add_use_case(UseCase.GET_DISTRIBUTION, self.calculate_distr_uc)
        UseCaseRepository.add_use_case(UseCase.GET_CORRELATION_MATRIX, self.get_correlation_matrix_uc)
        UseCaseRepository.add_use_case(UseCase.ENCODE_DATASET, self.encode_dataset_uc)
        UseCaseRepository.add_use_case(UseCase.CLEAN_DATASET, self.clean_dataset_uc)
        UseCaseRepository.add_use_case(UseCase.SPLIT_TRAIN_TEST, self.train_test_split_uc)
        UseCaseRepository.add_use_case(UseCase.FIT_PREDICT_MODEL, self.fit_predict_uc)
        UseCaseRepository.add_use_case(UseCase.EVALUATE_MODELS, self.evaluate_models_uc)
        UseCaseRepository.add_use_case(UseCase.DISPLAY, self.display_uc)
        UseCaseRepository.add_use_case(UseCase.DRAW_STATISTICAL_DATA, self.draw_statistical_data_use_case)

        self.send_msg_uc = self.create_send_message_use_case(self.chat)
        self.bind_tools_uc = self.create_bind_tools_use_case(self.tool_repository, self.chat)

        self.bind_tools_uc.bind_tools()

        self.appl_logic = ApplController(self.add_memory_uc, self.get_memories_uc, self.display_uc, self.response_handler,
                                    self.send_msg_uc, self.get_user_message_uc)

    def start_the_system(self):
        self.appl_logic.activate()
