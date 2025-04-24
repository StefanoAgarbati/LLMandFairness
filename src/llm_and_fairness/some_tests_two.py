from src.llm_and_fairness.appl_logic.appl_controller import ApplController
from src.llm_and_fairness.chat.chat_factory import ChatModelType, ChatFactory
from src.llm_and_fairness.datasets.dataset_repository import DatasetRepository
from src.llm_and_fairness.memory.memory_repository import MemoryRepository
from src.llm_and_fairness.messages.user_message import UserMessage
from src.llm_and_fairness.output_device.output_device_factory import OutputDeviceType, OutputDeviceFactory
from src.llm_and_fairness.tools.tool_repository_factory import ToolRepositoryType, ToolRepositoryFactory
from src.llm_and_fairness.use_cases.add_memory_use_case import AddMemoryUseCase
from src.llm_and_fairness.use_cases.bind_tools_use_case import BindToolsToChatUseCase
from src.llm_and_fairness.use_cases.calculate_distribution_use_case import CalculateDistributionUseCase
from src.llm_and_fairness.use_cases.get_memories_use_case import GetMemoriesUseCase
from src.llm_and_fairness.use_cases.handle_response_use_case import HandleResponseUseCase
from src.llm_and_fairness.use_cases.load_dataset_use_case import LoadDatasetUseCase
from src.llm_and_fairness.use_cases.send_message_use_case import SendMessageUseCase
from src.llm_and_fairness.use_cases.use_case_repository import UseCaseRepository, UseCase


class SystemConfig:
    chat_type = ChatModelType.GOOGLE
    model_name = 'gemini-2.0-flash'
    api_key = 'AIzaSyCNfAQnkwlkPZbE_CTIn-GSQPks-fmQMkY'
    out_dev_type = OutputDeviceType.Standard
    tool_repo_type = ToolRepositoryType.LANGCHAIN

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

def create_memory_repository() :
    return MemoryRepository()

def create_add_memory_use_case(memory_repository):
    return AddMemoryUseCase(memory_repository)

def create_get_memories_use_case(memory_repository):
    return GetMemoriesUseCase(memory_repository)

def create_system():
    chat = create_chat(SystemConfig.chat_type, SystemConfig.model_name,SystemConfig.api_key)
    output_device = create_output_device(SystemConfig.out_dev_type)
    tool_repository = create_tool_repository(SystemConfig.tool_repo_type)
    dataset_repository = create_dataset_repository()
    load_dataset_uc = create_load_dataset_use_case(dataset_repository)
    calculate_distr_uc = create_calculate_distr_use_case(dataset_repository)
    response_handler = create_response_handler(tool_repository)
    memory_repository = create_memory_repository()
    add_memory_uc = create_add_memory_use_case(memory_repository)
    get_memories_uc = create_get_memories_use_case(memory_repository)

    UseCaseRepository.add_use_case(UseCase.LOAD_DATASET, load_dataset_uc)
    UseCaseRepository.add_use_case(UseCase.GET_DISTRIBUTION,calculate_distr_uc)

    send_msg_uc = create_send_message_use_case(chat)
    bind_tools_uc = create_bind_tools_use_case(tool_repository, chat)

    bind_tools_uc.bind_tools()

    applLogic = ApplController(add_memory_uc,get_memories_uc,output_device,response_handler,send_msg_uc)
    applLogic.execute()


create_system()