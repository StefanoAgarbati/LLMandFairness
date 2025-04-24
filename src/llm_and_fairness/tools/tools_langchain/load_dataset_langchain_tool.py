import pandas as pd
from langchain_core.tools import tool

from src.llm_and_fairness.use_cases.use_case_repository import UseCaseRepository, UseCase


class LoadDatasetLangchainTool:

    def __init__(self, load_dataset_uc):
        self.load_dataset_uc = load_dataset_uc

    @tool(response_format="content_and_artifact")
    def load_dataset(dataset_name: str) -> tuple[str, pd.DataFrame]:
        """Load a csv dataset from its name"""
        data = UseCaseRepository.create(UseCase.LOAD_DATASET).load_dataset(dataset_name)
        content = f"Dataset {dataset_name} caricato con successo"
        return content, data