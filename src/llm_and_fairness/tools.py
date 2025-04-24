from support import DatasetLoader, DatasetFactory
from statis.statisdomain import StatisticsSupport, Distribution
from langchain_core.tools import tool
import pandas as pd
from typing import Tuple, Type
import inspect


def toolDispatcher(data):
    toolname = data['name']
    match toolname:
        case "loadDataset":
            return loadDataset.invoke(data)


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
    tools = [loadDataset, somma, get_distribution]
    return tools


@tool(response_format="content_and_artifact")
def loadDataset(pathname: str, columnspath: str) -> Tuple[str, pd.DataFrame]:
    """Load a csv dataset from a file using file's path name"""
    data = DatasetLoader.create_dataset(pathname, columnspath)
    content = "Dataset caricato con successo"
    return (content, data)


@tool(response_format="content_and_artifact")
def load_dataset(dataset_name: str) -> Tuple[str, pd.DataFrame]:
    """Load a csv dataset from its name"""
    data = DatasetFactory.create_dataset(dataset_name)
    content = f"Dataset {dataset_name} caricato con successo"
    return (content, data)


@tool(response_format="content_and_artifact")
def get_distribution(attribute_name: str) -> Tuple[str, Distribution]:
    """Calcola la distribuzione di frequenza degli attributi presenti nel dataset"""
    #data = support.get_distribution(attribute_name, 'frequency')
    #content = f"Ecco la distribuzione relativa all'attributo {attribute_name}"
    return ("", None)


@tool(response_format="content_and_artifact")
def somma(a: int, b: int) -> int:
    """somma due numeri interi"""
    data = a + b
    content = f"Somma -> {a} + {b} = {data}"
    return content, data
