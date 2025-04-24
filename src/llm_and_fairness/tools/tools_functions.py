from langchain_core.tools import tool
import pandas as pd

from src.llm_and_fairness.support import DatasetLoader
from src.llm_and_fairness.use_cases.use_case_repository import UseCaseRepository, UseCase

dataset_service = None

def toolDispatcher(data):
    toolname = data['name']
    match toolname:
        case "loadDataset":
            return loadDataset.invoke(data)

def get_available_tools_names():
    names = ['somma', 'load_dataset', 'get_distribution']
    return names

def get_tool_by_name(toolname):
    match toolname:
        case 'loadDataset':
            return loadDataset
        case 'get_distribution':
            return get_distribution
        case 'somma':
            return somma
        case 'load_dataset':
            return load_dataset
        case _:
            return None


def get_all_tools():
    tools = [load_dataset, somma, get_distribution]
    return tools


@tool(response_format="content_and_artifact")
def loadDataset(pathname: str, columnspath: str) -> tuple[str, pd.DataFrame]:
    """Load a csv dataset from a file using file's path name"""
    data = DatasetLoader.create_dataset(pathname, columnspath)
    content = "Dataset caricato con successo"
    return content, data


@tool(response_format="content_and_artifact")
def load_dataset(dataset_name: str) -> tuple[str, pd.DataFrame]:
    """Load a csv dataset from its name"""
    data = UseCaseRepository.get_use_case_by_name(UseCase.LOAD_DATASET).load_dataset(dataset_name)
    content = f"Dataset {dataset_name} caricato con successo"
    return content, data


@tool(response_format="content_and_artifact")
def get_distribution(attribute_name: str, dataset_name: str) -> tuple[str, pd.Series]:
    """Calcola la distribuzione di frequenza di un attributo presente nel dataset"""
    data = UseCaseRepository.get_use_case_by_name(UseCase.GET_DISTRIBUTION).calculate_frequency_distribution(dataset_name, attribute_name)
    content = f"Ecco la distribuzione relativa all'attributo {attribute_name}: {data}"
    return content, data


@tool(response_format="content_and_artifact")
def somma(a: int, b: int) -> tuple[str, int]:
    """somma due numeri interi"""
    data = a + b
    content = f"Somma -> {a} + {b} = {data}"
    return content, data
