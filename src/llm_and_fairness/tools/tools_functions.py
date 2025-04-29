from langchain_core.tools import tool
import pandas as pd

from ML.prediction import Prediction
from ML.split import Split
from support import DatasetLoader
from use_cases.use_case_repository import UseCaseRepository, UseCase

def get_available_tools_names():
    names = ['somma', 'load_dataset', 'get_distribution', 'get_correlation_matrix', 'encode_dataset',
             'clean_dataset', 'esegui_codifica_dataset', 'split_dataset_in_train_test_set',
             'addestra_un_modello_e_fai_una_previsione', 'calculate_the_distributions_of_all_attributes',
             'valuta_modelli_su_dataset_rispetto_a_target', 'disegna_i_grafici_delle_distribuzioni_di_tutti_gli_attributi',
             'disegna_la_matrice_di_correlazione_come_heatmap']
    return names

def get_tool_by_name(toolname):
    match toolname:
        case 'loadDataset':
            return loadDataset
        case 'get_distribution':
            return get_distribution
        case 'calculate_the_distributions_of_all_attributes':
            return calculate_the_distributions_of_all_attributes
        case 'get_correlation_matrix':
            return get_correlation_matrix
        case 'encode_dataset':
            return encode_dataset
        case 'esegui_codifica_dataset':
            return esegui_codifica_dataset
        case 'clean_dataset':
            return clean_dataset
        case 'split_dataset_in_train_test_set':
            return split_dataset_in_train_test_set
        case 'addestra_un_modello_e_fai_una_previsione':
            return addestra_un_modello_e_fai_una_previsione
        case 'valuta_modelli_su_dataset_rispetto_a_target':
            return valuta_modelli_su_dataset_rispetto_a_target
        case 'disegna_i_grafici_delle_distribuzioni_di_tutti_gli_attributi':
            return disegna_i_grafici_delle_distribuzioni_di_tutti_gli_attributi
        case 'disegna_la_matrice_di_correlazione_come_heatmap':
            return disegna_la_matrice_di_correlazione_come_heatmap
        case 'somma':
            return somma
        case 'load_dataset':
            return load_dataset
        case _:
            return None


def get_all_tools():
    tools =[]
    for name in get_available_tools_names():
        tool = get_tool_by_name(name)
        tools.append(tool)
    return tools

    # tools = [load_dataset, somma, get_distribution, get_correlation_matrix, encode_dataset,
    #          clean_dataset, esegui_codifica_dataset, split_dataset_in_train_test_set,
    #          addestra_un_modello_e_fai_una_previsione, calculate_the_distributions_of_all_attributes,
    #          valuta_modelli_su_dataset_rispetto_a_target, disegna_i_grafici_delle_distribuzioni_di_tutti_gli_attributi,
    #          disegna_la_matrice_di_correlazione_come_heatmap]
    # return tools


@tool(response_format="content_and_artifact")
def loadDataset(pathname: str, columnspath: str) -> tuple[str, pd.DataFrame]:
    """Load a csv dataset from a file using file's path name"""
    data = DatasetLoader.create_dataset(pathname, columnspath)
    content = "Dataset caricato con successo"
    return content, data


@tool(response_format="content_and_artifact")
def load_dataset(dataset_name: str) -> tuple[str, pd.DataFrame]:
    """Load a csv dataset from its name"""
    print("Load dataset tool called")
    data = UseCaseRepository.get_use_case_by_name(UseCase.LOAD_DATASET).load_dataset(dataset_name)
    display_uc = UseCaseRepository.get_use_case_by_name(UseCase.DISPLAY)
    display_uc.display_markdown(f"Il dataset {dataset_name} è stato caricato.")
    display_uc.display(data)
    content = f"Dataset {dataset_name} caricato con successo"
    return content, data


@tool(response_format="content_and_artifact")
def clean_dataset(dataset_name: str) -> tuple[str, pd.DataFrame]:
    """Esegue operazioni di pulizia (cleaning) su di un dataset"""
    data = UseCaseRepository.get_use_case_by_name(UseCase.CLEAN_DATASET).clean_dataset(dataset_name)
    display_uc = UseCaseRepository.get_use_case_by_name(UseCase.DISPLAY)
    display_uc.display_markdown(f"Ho eseguito la pulizia del dataset {dataset_name}")
    display_uc.display(data)
    content = f"Il dataset {dataset_name} è stato pulito"
    #print(f"Tool clean_dataset eseguito su {dataset_name}")
    return content, data

@tool(response_format="content_and_artifact")
def calculate_the_distributions_of_all_attributes(dataset_name: str) -> tuple[str, list[pd.Series]]:
    """Calcola la distribuzione di frequenza di tutti gli attributi presenti nel dataset"""
    data = UseCaseRepository.get_use_case_by_name(UseCase.GET_DISTRIBUTION).calculate_all_frequency_distributions(
        dataset_name)
    display_uc = UseCaseRepository.get_use_case_by_name(UseCase.DISPLAY)
    display_uc.display_markdown(f"Quelle che seguono sono le distribuzioni di tutti gli attributi del dataset {dataset_name}")
    for distri in data:
        display_uc.display(data)

    content = f"Ecco le distribuzioni di tutti gli attributi presenti nel dataset {dataset_name}:\n"
    for item in data:
        content += item.to_json() + "\n"
    return content, data

@tool(response_format="content_and_artifact")
def get_distribution(attribute_name: str, dataset_name: str) -> tuple[str, pd.Series]:
    """Calcola la distribuzione di frequenza di un attributo presente nel dataset"""
    data = UseCaseRepository.get_use_case_by_name(UseCase.GET_DISTRIBUTION).calculate_frequency_distribution(dataset_name, attribute_name)
    content = f"Ecco la distribuzione relativa all'attributo {attribute_name}:\n {data.to_json()}"
    return content, data


@tool(response_format="content_and_artifact")
def get_correlation_matrix(dataset_name: str) -> tuple[str, pd.DataFrame]:
    """Calcola la matrice di correlazione relativa ad un dataset"""
    data = UseCaseRepository.get_use_case_by_name(UseCase.GET_CORRELATION_MATRIX).get_correlation_matrix(dataset_name)
    display_uc = UseCaseRepository.get_use_case_by_name(UseCase.DISPLAY)
    display_uc.display_markdown(f"Questa è la matrice di correlazione relativa agli attributi del dataset {dataset_name}")
    display_uc.display(data)
    content = f"Ecco la matrice di correlazione relativa al dataset {dataset_name}\n {data.to_json()}"
    return content, data

@tool(response_format="content_and_artifact")
def esegui_codifica_dataset(dataset_name: str) -> tuple[str, pd.DataFrame]:
    """trasforma un dataset in forma numerica"""
    data = UseCaseRepository.get_use_case_by_name(UseCase.ENCODE_DATASET).encode_dataset(dataset_name)
    content = f"Il dataset {dataset_name} è stato codificato (encoded)\n"
    print(f"Tool encode_dataset eseguito su {dataset_name}")
    return content, data


@tool(response_format="content_and_artifact")
def encode_dataset(dataset_name: str) -> tuple[str, pd.DataFrame]:
    """trasforma un dataset in forma numerica"""
    data = UseCaseRepository.get_use_case_by_name(UseCase.ENCODE_DATASET).encode_dataset(dataset_name)
    content = f"Il dataset {dataset_name} è stato codificato (encoded)\n"
    print(f"Tool encode_dataset eseguito su {dataset_name}")
    return content, data

@tool(response_format="content_and_artifact")
def split_dataset_in_train_test_set(dataset_name:str, target: list | str) -> tuple[str, Split]:
    """suddivide un dataset in due parti: una parte per il training e l'altra per il testing di un modello"""
    data = UseCaseRepository.get_use_case_by_name(UseCase.SPLIT_TRAIN_TEST).split(dataset_name, target)
    content = (f"Il dataset {dataset_name} è stato suddiviso negli insiemi train e test."
               f"Ora è possibile addestrare un modello")
    print(f"SplitDatasetTool:\n"
          f"y_test:\n"
          f"{data.get_y_test()}")
    return content, data


@tool(response_format="content_and_artifact")
def addestra_un_modello_e_fai_una_previsione(test_set_name:str) -> tuple[str, Prediction]:
    """addestra un modello su di un training set e tenta una previsione usando un test set"""
    data = UseCaseRepository.get_use_case_by_name(UseCase.FIT_PREDICT_MODEL).fit_predict(test_set_name)
    content = f"Il modello è stato addestrato sul test set {test_set_name} e ha prodotto una previsione"
    print(f"Predictions:\n{data.get_y_pred()}")
    return content, data

@tool(response_format="content_and_artifact")
def valuta_modelli_su_dataset_rispetto_a_target(dataset_name: str, target: str) -> tuple[str, list[dict]]:
    """valuta alcuni modelli di machine learning"""
    data = UseCaseRepository.get_use_case_by_name(UseCase.EVALUATE_MODELS).evaluate_models(dataset_name, target)
    content = f"Ecco la valutazione dei modelli:\n"
    for item in data:
        content += f"Modello {item['model_name']}\n"
        content += f"{item['score'].mean()}\n"
    return content, data

@tool(response_format="content_and_artifact")
def disegna_i_grafici_delle_distribuzioni_di_tutti_gli_attributi(dataset_name: str) -> tuple[str, list]:
    """Disegna i grafici delle distribuzione di tutti gli attributi di un dataset"""
    data = UseCaseRepository.get_use_case_by_name(UseCase.DRAW_STATISTICAL_DATA).draw_all_distributions(dataset_name)
    display_uc = UseCaseRepository.get_use_case_by_name(UseCase.DISPLAY)
    display_uc.display_markdown(f"Ecco i grafici che mostrano le distribuzioni di tutti gli attributi del dataset {dataset_name}")
    for figure in data:
        display_uc.display_figure(figure)

    content = f"Ecco i grafici che mostrano le distribuzioni di tutte le variabili del dataset {dataset_name}"
    return content, data


@tool(response_format="content_and_artifact")
def disegna_la_matrice_di_correlazione_come_heatmap(dataset_name: str) -> tuple[str, list]:
    """Disegna la matrice di correlazione di un dataset come una heatmap"""
    data = UseCaseRepository.get_use_case_by_name(UseCase.DRAW_STATISTICAL_DATA).draw_correlation_matrix(dataset_name)
    display_uc = UseCaseRepository.get_use_case_by_name(UseCase.DISPLAY)
    display_uc.display_markdown(
        f"Questa è la matrice di correlazione relativa agli attributi del dataset {dataset_name} in forma di heatmap")
    display_uc.display_figure(data)

    content = f"Ho disegnato la heatmap rappresentativa della matrice di correlazione del dataset {dataset_name}"
    return content, data

@tool(response_format="content_and_artifact")
def somma(a: int, b: int) -> tuple[str, int]:
    """somma due numeri interi"""
    data = a + b
    msg = f"Somma {a} + {b} = {data}"
    display_uc = UseCaseRepository.get_use_case_by_name(UseCase.DISPLAY)
    display_uc.display_markdown(msg)
    content = msg
    return content, data
