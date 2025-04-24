import pandas as pd
from langchain_core.tools import tool

from src.llm_and_fairness.statis.statisdomain import Distribution
from src.llm_and_fairness.support import DatasetFactory
from src.llm_and_fairness.use_cases.use_case_repository import UseCaseRepository, UseCase


class ToolsFunctionsLangchain:


    def get_available_tools_names(self):
        names = ['somma', 'load_dataset', 'get_distribution']
        return names


    def get_tool_by_name(self, toolname):
        match toolname:
            case 'get_distribution':
                return ToolsFunctionsLangchain.get_distribution
            case 'somma':
                return ToolsFunctionsLangchain.somma
            case 'load_dataset':
                return ToolsFunctionsLangchain.load_dataset
            case _:
                return None

    def get_all_tools(self):
        tools = [ToolsFunctionsLangchain.load_dataset, ToolsFunctionsLangchain.somma,
                 ToolsFunctionsLangchain.get_distribution]
        return tools


    @tool(response_format="content_and_artifact")
    def load_dataset(dataset_name: str) -> tuple[str, pd.DataFrame]:
        """Load a csv dataset from its name"""
        data = UseCaseRepository.get_use_case(UseCase.LOAD_DATASET).load_dataset(dataset_name)
        content = f"Dataset {dataset_name} caricato con successo"
        return content, data

    @tool(response_format="content_and_artifact")
    def get_distribution(dataset_name: str, attribute_name: str) -> tuple[str, pd.Series]:
        """Calcola la distribuzione di frequenza degli attributi presenti nel dataset"""
        data = UseCaseRepository.get_use_case(UseCase.GET_DISTRIBUTION).calculate_frequency_distribution(dataset_name, attribute_name)
        content = f"Ecco la distribuzione relativa all'attributo {attribute_name}"
        return content, data

    @tool(response_format="content_and_artifact")
    def somma(a: int, b: int) -> tuple[str, int]:
        """somma due numeri interi"""
        data = a + b
        content = f"Somma -> {a} + {b} = {data}"
        return content, data
