from collections import namedtuple

import pandas as pd

from ML.prediction import Prediction
from ML.split import Split
from support import DatasetLoader
from use_cases.use_case_repository import UseCaseRepository, UseCase


def get_available_tools_names():
    names = ['somma', 'load_dataset', 'get_distribution', 'get_correlation_matrix', 'encode_dataset',
             'clean_dataset', 'esegui_codifica_dataset', 'split_dataset_in_train_test_set',
             'addestra_un_modello_e_fai_una_previsione_usando_uno_split',
             'calculate_the_distributions_of_all_attributes',
             'valuta_modelli_su_dataset_rispetto_a_target',
             'disegna_i_grafici_delle_distribuzioni_di_tutti_gli_attributi',
             'get_correlation_heatmap', 'rileva_eventuali_variabili_proxy',
             'available_models_for',
             'evaluate_models', 'metriche_di_performance_disponibili_per', 'esegui_trasformazione_inversa',
             'addestra_un_modello_e_fai_una_previsione_su_dataset_e_target',
             'mostra_metriche_di_fairness_di_gruppo_disponibili',
             'mostra_metriche_di_fairness_aggregate_disponibili', 'calcola_le_metriche_di_fairness_di_gruppo']
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
        case 'addestra_un_modello_e_fai_una_previsione_usando_uno_split':
            return addestra_un_modello_e_fai_una_previsione_usando_uno_split
        case 'valuta_modelli_su_dataset_rispetto_a_target':
            return valuta_modelli_su_dataset_rispetto_a_target
        case 'disegna_i_grafici_delle_distribuzioni_di_tutti_gli_attributi':
            return disegna_i_grafici_delle_distribuzioni_di_tutti_gli_attributi
        case 'get_correlation_heatmap':
            return get_correlation_heatmap
        case 'rileva_eventuali_variabili_proxy':
            return rileva_eventuali_variabili_proxy
        case 'available_models_for':
            return available_models_for
        case 'evaluate_models':
            return evaluate_models
        case 'metriche_di_performance_disponibili_per':
            return metriche_di_performance_disponibili_per
        case 'esegui_trasformazione_inversa':
            return esegui_trasformazione_inversa
        case 'addestra_un_modello_e_fai_una_previsione_su_dataset_e_target':
            return addestra_un_modello_e_fai_una_previsione_su_dataset_e_target
        case 'mostra_metriche_di_fairness_di_gruppo_disponibili':
            return mostra_metriche_di_fairness_di_gruppo_disponibili
        case 'mostra_metriche_di_fairness_aggregate_disponibili':
            return mostra_metriche_di_fairness_aggregate_disponibili
        case 'calcola_le_metriche_di_fairness_di_gruppo':
            return calcola_le_metriche_di_fairness_di_gruppo
        case 'somma':
            return somma
        case 'load_dataset':
            return load_dataset
        case _:
            return None

def get_all_tools():
    tools = []
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

def loadDataset(pathname: str, columnspath: str) -> tuple[str, pd.DataFrame]:
    """Load a csv dataset from a file using file's path name"""
    data = DatasetLoader.create_dataset(pathname, columnspath)
    content = "Dataset caricato con successo"
    return namedtuple("ToolExecutionResult", ["content", "artifact"])(content, data)

def load_dataset(dataset_name: str) -> tuple[str, pd.DataFrame]:
    """Load a csv dataset from its name"""
    # print("Load dataset tool called")
    data = UseCaseRepository.get_use_case_by_name(UseCase.LOAD_DATASET).load_dataset(dataset_name)
    display_uc = UseCaseRepository.get_use_case_by_name(UseCase.DISPLAY)
    display_uc.display_markdown(f"Il tuo dataset {dataset_name} è stato caricato.")
    display_uc.display(data)
    content = f"Il tuo dataset {dataset_name} è stato caricato con successo"
    return namedtuple("ToolExecutionResult", ["content", "artifact"])(content, data)

def clean_dataset(dataset_name: str) -> tuple[str, pd.DataFrame]:
    """Esegue operazioni di pulizia (cleaning) su di un dataset"""
    data = UseCaseRepository.get_use_case_by_name(UseCase.CLEAN_DATASET).clean_dataset(dataset_name)
    display_uc = UseCaseRepository.get_use_case_by_name(UseCase.DISPLAY)
    display_uc.display_markdown(f"Ho eseguito la pulizia del tuo dataset {dataset_name}")
    display_uc.display(data)
    content = f"Il tuo dataset {dataset_name} è stato pulito"
    # print(f"Tool clean_dataset eseguito su {dataset_name}")
    return namedtuple("ToolExecutionResult", ["content", "artifact"])(content, data)

def calculate_the_distributions_of_all_attributes(dataset_name: str) -> tuple[str, list[pd.Series]]:
    """Calcola la distribuzione di frequenza di tutti gli attributi presenti nel dataset"""
    #print(f"calculate_distributions_tool->invoked with dataset->{dataset_name}")
    data = UseCaseRepository.get_use_case_by_name(UseCase.GET_DISTRIBUTION).calculate_all_frequency_distributions(
        dataset_name)
    display_uc = UseCaseRepository.get_use_case_by_name(UseCase.DISPLAY)
    display_uc.display_markdown(
        f"Quelle che seguono sono le distribuzioni di tutti gli attributi del tuo dataset {dataset_name}")
    for distri in data:
        display_uc.display(distri)

    content = f"Ecco le distribuzioni di tutti gli attributi presenti nel tuo dataset {dataset_name}:\n"
    for item in data:
        content += item.to_json() + "\n"
    return namedtuple("ToolExecutionResult", ["content", "artifact"])(content, data)

def get_distribution(attribute_name: str, dataset_name: str) -> tuple[str, pd.Series]:
    """Calcola la distribuzione di frequenza di un attributo presente nel dataset"""
    data = UseCaseRepository.get_use_case_by_name(UseCase.GET_DISTRIBUTION).calculate_frequency_distribution(
        dataset_name, attribute_name)
    content = f"Ecco la distribuzione relativa all'attributo {attribute_name}:\n {data.to_json()}"
    return namedtuple("ToolExecutionResult", ["content", "artifact"])(content, data)


def get_correlation_matrix(dataset_name: str) -> tuple[str, pd.DataFrame]:
    """
    Calcola la matrice di correlazione relativa ad un dataset
    Richiede il nome del dataset come paramentro
    """
    data = UseCaseRepository.get_use_case_by_name(UseCase.GET_CORRELATION_MATRIX).get_correlation_matrix(
        dataset_name)
    display_uc = UseCaseRepository.get_use_case_by_name(UseCase.DISPLAY)
    display_uc.display_markdown(
        f"Questa è la matrice di correlazione relativa agli attributi del tuo dataset {dataset_name}")
    display_uc.display(data)
    content = f"Ecco la matrice di correlazione relativa al tuo dataset {dataset_name}\n{data.to_json()}"
    return namedtuple("ToolExecutionResult", ["content", "artifact"])(content, data)


def esegui_codifica_dataset(dataset_name: str) -> tuple[str, pd.DataFrame]:
    """
    Esegue la codifica di un dataset
    Richiede come parametro il nome del dataset
    """
    data = UseCaseRepository.get_use_case_by_name(UseCase.ENCODE_DATASET).encode_dataset(dataset_name)
    display_uc = UseCaseRepository.get_use_case_by_name(UseCase.DISPLAY)
    display_uc.display_markdown(
        f"Il tuo dataset {dataset_name} è stato codificato")
    display_uc.display(data)
    content = f"Il tuo dataset {dataset_name} è stato codificato (encoded)\n"
    # print(f"Tool encode_dataset eseguito su {dataset_name}")
    return namedtuple("ToolExecutionResult", ["content", "artifact"])(content, data)


def esegui_trasformazione_inversa(dataset_name: str) -> tuple[str, pd.DataFrame]:
    """
    esegue la decodifica di un dataset
    """
    data = UseCaseRepository.get_use_case_by_name(UseCase.ENCODE_DATASET).decode_dataset(dataset_name)
    display_uc = UseCaseRepository.get_use_case_by_name(UseCase.DISPLAY)
    display_uc.display_markdown(
        f"Il tuo dataset {dataset_name} è stato decodificato wowowow")
    display_uc.display(data)
    content = f"Il tuo dataset {dataset_name} è stato decodificato (decoded)\n"
    # print(f"Tool encode_dataset eseguito su {dataset_name}")
    return namedtuple("ToolExecutionResult", ["content", "artifact"])(content, data)


def encode_dataset(dataset_name: str) -> tuple[str, pd.DataFrame]:
    """trasforma un dataset in forma numerica"""
    data = UseCaseRepository.get_use_case_by_name(UseCase.ENCODE_DATASET).encode_dataset(dataset_name)
    display_uc = UseCaseRepository.get_use_case_by_name(UseCase.DISPLAY)
    display_uc.display_markdown(
        f"Il tuo dataset {dataset_name} è stato codificato")
    display_uc.display(data)
    content = f"Il tuo dataset {dataset_name} è stato codificato (encoded)\n"
    # print(f"Tool encode_dataset eseguito su {dataset_name}")
    return namedtuple("ToolExecutionResult", ["content", "artifact"])(content, data)


def split_dataset_in_train_test_set(dataset_name: str, target: list | str) -> tuple[str, Split]:
    """
    suddivide un dataset in due parti: una parte per il training e l'altra per il testing di un modello
    Esegue lo split di un dataset in train e test set.
    Richiede il nome del dataset e il nome della variabile target
    """
    data = UseCaseRepository.get_use_case_by_name(UseCase.SPLIT_TRAIN_TEST).split(dataset_name, target)
    display_uc = UseCaseRepository.get_use_case_by_name(UseCase.DISPLAY)
    display_uc.display_markdown(f"Ho eseguito lo split del tuo dataset {dataset_name}")
    content = (
        f"Il tuo dataset {dataset_name} è stato suddiviso negli insiemi train e test rappresentati dallo split {dataset_name}."
        f"Ora è possibile addestrare un modello")
    """print(f"SplitDatasetTool:\n"
          f"y_test:\n"
          f"{data.get_y_test()}")"""
    return namedtuple("ToolExecutionResult", ["content", "artifact"])(content, data)


def addestra_un_modello_e_fai_una_previsione_su_dataset_e_target(model_name: str, dataset_name: str) -> tuple[
    str, Prediction]:
    """
    addestra un modello e fa una previsione utilizzando un dataset.
    Richiede il nome di un modello e il nome di un dataset
    """
    data = UseCaseRepository.get_use_case_by_name(UseCase.TRAIN_MODEL_MAKE_PREDICTION).fit_predict(model_name,
                                                                                                   dataset_name)
    display_uc = UseCaseRepository.get_use_case_by_name(UseCase.DISPLAY)
    display_uc.display_markdown(f"Il modello {model_name} è stato addestrato ed ha prodotto una previsione")
    display_uc.display_markdown(f"Prediction:\n{data.get_y_pred()}")
    content = f"Il modello {model_name} è stato addestrato sul test set {dataset_name} e ha prodotto una previsione:\n"
    content += f"Predictions:\n{data.get_y_pred()}"
    # print(f"Predictions:\n{data.get_y_pred()}")
    return namedtuple("ToolExecutionResult", ["content", "artifact"])(content, data)


def addestra_un_modello_e_fai_una_previsione_usando_uno_split(split_name: str) -> tuple[str, Prediction]:
    """addestra un modello e fa una previsione utilizzando uno split"""
    data = UseCaseRepository.get_use_case_by_name(UseCase.FIT_PREDICT_MODEL).fit_predict(split_name)
    display_uc = UseCaseRepository.get_use_case_by_name(UseCase.DISPLAY)
    display_uc.display_markdown(f"Il modello è stato addestrato ed ha prodotto una previsione")
    display_uc.display_markdown(f"Prediction:\n{data.get_y_pred()}")
    content = f"Il modello è stato addestrato sul test set {split_name} e ha prodotto una previsione:\n"
    content += f"Predictions:\n{data.get_y_pred()}"
    # print(f"Predictions:\n{data.get_y_pred()}")
    return namedtuple("ToolExecutionResult", ["content", "artifact"])(content, data)


def valuta_modelli_su_dataset_rispetto_a_target(dataset_name: str, target: str) -> tuple[str, list[dict]]:
    """
    Valuta alcuni modelli di machine learning.
    Richiede il nome di un dataset e il nome della variabile target
    """
    data = UseCaseRepository.get_use_case_by_name(UseCase.EVALUATE_MODELS).evaluate_models(dataset_name, target)
    display_uc = UseCaseRepository.get_use_case_by_name(UseCase.DISPLAY)
    display_uc.display_markdown(f"Ecco la valutazione dei modelli:\n")
    msg = ''
    for item in data:
        display_uc.display_markdown(f"Modello {item['model_name']}\n")
        display_uc.display(f"{item['score'].mean()}\n")
    content = f"Ecco la valutazione dei modelli:\n"
    for item in data:
        content += f"Modello {item['model_name']}\n"
        content += f"{item['score'].mean().to_json()}\n"
    return namedtuple("ToolExecutionResult", ["content", "artifact"])(content, data)


def evaluate_models(models: str, metrics: str, dataset_name: str, target: str) -> tuple[str, list[dict]]:
    """
    Valuta alcuni modelli di machine learning.
    Richiede una stringa che riporta i nomi dei modelli, una stringa che riporta le metriche, il nome di un dataset
    e il nome della variabile target
    """
    data = UseCaseRepository.get_use_case_by_name(UseCase.MODELS_EVALUATION).evaluate_models(models, metrics,
                                                                                             dataset_name, target)
    display_uc = UseCaseRepository.get_use_case_by_name(UseCase.DISPLAY)
    display_uc.display_markdown(f"Ecco la valutazione dei modelli:\n")
    msg = ''
    for item in data:
        display_uc.display_markdown("Modello " + item['model_name'] + ":")
        display_uc.display(item['score'].mean())
    content = "Ecco la valutazione dei modelli:\n"
    for item in data:
        content += "Modello" + " {item['model_name']}\n"
        content += item['score'].mean().to_json() + "\n"
    return namedtuple("ToolExecutionResult", ["content", "artifact"])(content, data)


def disegna_i_grafici_delle_distribuzioni_di_tutti_gli_attributi(dataset_name: str) -> tuple[str, list]:
    """
    Disegna i grafici delle distribuzioni di tutti gli attributi di un dataset
    Richiede come parametro il nome del dataset
    """
    data = UseCaseRepository.get_use_case_by_name(UseCase.DRAW_STATISTICAL_DATA).draw_all_distributions(
        dataset_name)
    display_uc = UseCaseRepository.get_use_case_by_name(UseCase.DISPLAY)
    display_uc.display_markdown(
        f"Ecco i grafici che mostrano le distribuzioni di tutti gli attributi del tuo dataset {dataset_name}")
    for figure in data:
        display_uc.display_figure(figure)

    content = f"Ecco i grafici che mostrano le distribuzioni di tutte le variabili, attributi del tuo dataset {dataset_name}"
    return namedtuple("ToolExecutionResult", ["content", "artifact"])(content, data)


def get_correlation_heatmap(dataset_name: str) -> tuple[str, list]:
    """
    Disegna la matrice di correlazione come una heatmap di un dataset
    Richiede il nome del dataset come parametro
    """
    data = UseCaseRepository.get_use_case_by_name(UseCase.DRAW_STATISTICAL_DATA).draw_correlation_matrix(
        dataset_name)
    display_uc = UseCaseRepository.get_use_case_by_name(UseCase.DISPLAY)
    display_uc.display_markdown(
        f"Questa è la matrice di correlazione relativa agli attributi del tuo dataset {dataset_name} in forma di heatmap")
    display_uc.display_figure(data)

    content = f"Ho disegnato la heatmap rappresentativa della matrice di correlazione del tuo dataset {dataset_name}"
    return namedtuple("ToolExecutionResult", ["content", "artifact"])(content, data)


def rileva_eventuali_variabili_proxy(dataset_name: str) -> tuple[str, list]:
    """Rileva eventuali variabili proxy presenti nel dataset usando la mutual information"""
    data = UseCaseRepository.get_use_case_by_name(UseCase.DETECT_PROXY).detect_proxy_variables(dataset_name)
    display_uc = UseCaseRepository.get_use_case_by_name(UseCase.DISPLAY)
    content = ""
    display_uc.display_markdown(
        f"Ecco la mutual information di tutte le variabili del tuo dataset {dataset_name}")
    for detection in data:
        variable = detection.get_data('variable_name')
        msg = f"Mutual information per {variable}:\n"
        display_uc.display_markdown(msg)
        display_uc.display(detection.get_data('mutual_info'))
        content = msg + detection.get_data('mutual_info').to_json()

    return namedtuple("ToolExecutionResult", ["content", "artifact"])(content, data)


def available_models_for(problem_type: str) -> tuple[str, str]:
    """
    Restituisce l'elenco dei modelli disponibili per uno specifico problema di learning
    Fornisci come parametro il tipo di problema di learning specifico
    """
    data = UseCaseRepository.get_use_case_by_name(UseCase.GET_AVAILABLE_MODELS).get_available_models_for(
        problem_type)
    display_uc = UseCaseRepository.get_use_case_by_name(UseCase.DISPLAY)
    msg = f"Modelli disponibili per problemi di {problem_type} sono: " + data
    display_uc.display_markdown(msg)
    content = msg
    return namedtuple("ToolExecutionResult", ["content", "artifact"])(content, data)


def metriche_di_performance_disponibili_per(problema_di_learning: str) -> tuple[str, str]:
    """
    Restituisce l'elenco delle metriche di performance disponibili per uno specifico problema di learning.
    Richiede il nome del tipo di problema di learning
    """
    data = UseCaseRepository.get_use_case_by_name(UseCase.GET_AVAILABLE_METRICS).get_available_metrics_for(
        problema_di_learning)
    display_uc = UseCaseRepository.get_use_case_by_name(UseCase.DISPLAY)
    msg = f"Ecco le metriche disponibili per problemi di {problema_di_learning} : {data}\n"
    display_uc.display_markdown(msg)
    content = msg
    return namedtuple("ToolExecutionResult", ["content", "artifact"])(content, data)


def mostra_metriche_di_fairness_di_gruppo_disponibili(problem_type: str) -> tuple[str, str]:
    """
    Restituisce l'elenco delle metriche di fairness di gruppo disponibili per uno specifico problema di learning
    Richiede il nome del tipo di problema di learning
    """
    data = UseCaseRepository.get_use_case_by_name(UseCase.GET_AVAILABLE_FAIRNESS_METRICS).get_group_metrics(
        problem_type)
    display_uc = UseCaseRepository.get_use_case_by_name(UseCase.DISPLAY)
    msg = f"Ecco le metriche di fairness di gruppo disponibili per problemi di {problem_type} : {data}"
    display_uc.display_markdown(msg)
    # print("Tool metricheDiGruppo -> invoked with " + problem_type)
    content = msg
    return namedtuple("ToolExecutionResult", ["content", "artifact"])(content, data)

def mostra_metriche_di_fairness_aggregate_disponibili(problem_type: str) -> tuple[str, str]:
    """
    Restituisce l'elenco delle metriche di fairness aggregate disponibili per uno specifico problema di learning.
    Le metriche di fairness aggregate sono diverse da quelle di gruppo.
    Il parametro problem_type di tipo stringa rappresenta il tipo di problema di learning come ad esempio classificazione
    oppure regressione o clustering ecc....
    Richiede come parametro un corretto tipo di problema di learning
        """
    data = UseCaseRepository.get_use_case_by_name(UseCase.GET_AVAILABLE_FAIRNESS_METRICS).get_aggregated_metrics(
        problem_type)
    display_uc = UseCaseRepository.get_use_case_by_name(UseCase.DISPLAY)
    msg = f"Ecco le metriche di fairness aggregate disponibili per problemi di {problem_type} : {data}"
    display_uc.display_markdown(msg)
    content = '{"metriche di fairness aggregate disponibili":' + f"{data}" + "}"
    # print("Tool metricheAggregate -> invoked with " + problem_type)
    return namedtuple("ToolExecutionResult", ["content", "artifact"])(content, data)

def calcola_le_metriche_di_fairness_di_gruppo(metriche: str, sensible: str, dataset_name: str) -> tuple[str, list]:
    """
    Calcola le metriche di fairness di gruppo fornite attraverso il paramentro metriche.
    Il calcolo viene eseguito su tutti gli attributi sensibili di un dataset forniti attraverso il parametro sensible
    Per il parametro metriche fornisci una stringa composta da nomi separati da virgole
    Per il parametro sensible fornisci una stringa composta da nomi di attributi separati da virgole
    Per il parametro dataset_name fornisci il nome di un dataset
    """
    # print(f"calcola metriche di fairness di gruppo tool -> metriche: {metriche}, sensible: {sensible}, dataset: {dataset_name}")
    data = UseCaseRepository.get_use_case_by_name(UseCase.COMPUTE_FAIRNESS_METRICS).get_fairness_group_metrics(
        dataset_name, metriche, sensible)
    display_uc = UseCaseRepository.get_use_case_by_name(UseCase.DISPLAY)
    msg = "Ecco il calcolo delle metriche di fairness di gruppo per le variabili sensibili " + sensible + ":\n"
    content = msg
    display_uc.display_markdown(msg)
    for item in data:
        display_uc.display(item)
        content += item.to_json() + "\n"
    return namedtuple("ToolExecutionResult", ["content", "artifact"])(content, data)

def somma(a: int, b: int) -> tuple[str, int]:
    """somma due numeri interi"""
    data = a + b
    msg = f"Somma {a} + {b} = {data}"
    display_uc = UseCaseRepository.get_use_case_by_name(UseCase.DISPLAY)
    display_uc.display_markdown(msg)
    content = msg
    return namedtuple("ToolExecutionResult", ["content", "artifact"])(content, data)