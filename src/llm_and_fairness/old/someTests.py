from abc import ABC, abstractmethod
from typing import Type

#from chat import GoogleChatModel, ChatModelFactory, ChatModelType
#from main import ApplConfig
from src.llm_and_fairness.chat.chat_factory import ChatFactory, ChatModelType
from src.llm_and_fairness.datasets.dataset_repository import DatasetRepository
from src.llm_and_fairness.memory.memory_repository import MemoryRepository
from src.llm_and_fairness.messages.user_message import UserMessage
from src.llm_and_fairness.output_device.output_device_factory import OutputDeviceFactory, OutputDeviceType
from src.llm_and_fairness.tools.tool_repository_factory import ToolRepositoryFactory, ToolRepositoryType
from src.llm_and_fairness.tools.tools_functions_langchain import ToolsFunctionsLangchain
from src.llm_and_fairness.use_cases.add_memory_use_case import AddMemoryUseCase
from src.llm_and_fairness.use_cases.bind_tools_use_case import BindToolsToChatUseCase
from src.llm_and_fairness.use_cases.calculate_distribution_use_case import CalculateDistributionUseCase
from src.llm_and_fairness.use_cases.get_memories_use_case import GetMemoriesUseCase
from src.llm_and_fairness.use_cases.handle_response_use_case import HandleResponseUseCase
from src.llm_and_fairness.use_cases.load_dataset_use_case import LoadDatasetUseCase
from src.llm_and_fairness.use_cases.send_message_use_case import SendMessageUseCase
from src.llm_and_fairness.use_cases.use_case_repository import UseCaseRepository, UseCase
from support import DatasetFactory
from support import DatasetLoader

#chat = ChatModelFactory.createChatModel(ChatModelType.GOOGLE, ApplConfig.modelName, ApplConfig.apiKey)
#print(chat)

#ds = DatasetFactory.create_dataset("adult")
#print(ds)
"""api_key = "AIzaSyCNfAQnkwlkPZbE_CTIn-GSQPks-fmQMkY"
model_name = "gemini-2.0-flash"

chat = ChatFactory.create_chat(ChatModelType.GOOGLE, model_name, api_key)
user_message = UserMessage('Ciao, io sono Stefano ed oggi è Pasqua. Quindi buona Pasqua a te', {})

response = chat.sendMessage(user_message)
print(response.get_message())"""

"""tools = ToolsFunctionsLangchain()
a_tool = tools.get_tool_by_name('somma')
res = a_tool.invoke({
    "name": "somma",
    "args": {"a": 10, "b": 13},
    "id": 1,
    "type": "tool_call"
})
print(res)"""
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

    #send_msg_uc.send_message(UserMessage("Carica il dataset {dataset}", {"dataset":"adult"}))
    #send_msg_uc.send_message(UserMessage("Calcola la distribuzione dell'attributo {attributo} del dataset {dataset} e dimmi se noti disproporzioni" , {"attributo": "income", "dataset":"adult"}))
    #send_msg_uc.send_message(UserMessage("Noti delle disproporzioni nella distribuzione dell'attributo {attributo} del dataset {dataset}", {"attributo": "income", "dataset":"adult"}))

    user_message = UserMessage("Ciao io mi chiamo Stefano, buona giornata", {})
    output_device.out(user_message.get_message())
    add_memory_uc.add_memory(user_message.get_message())
    memories = get_memories_uc.get_memories()
    response = send_msg_uc.send_string_message(memories)
    add_memory_uc.add_memory(response.get_message())
    output_device.out(response.get_message())

    user_message = UserMessage("Non ricordo il mio nome, puoi dirmi tu qual'è?", {})
    output_device.out(user_message.get_message())
    add_memory_uc.add_memory(user_message.get_message())
    memories = get_memories_uc.get_memories()
    response = send_msg_uc.send_string_message(memories)
    add_memory_uc.add_memory(response.get_message())
    output_device.out(response.get_message())
    #send_msg_uc.send_message(UserMessage("Conosci il mio nome?", {}))

create_system()








