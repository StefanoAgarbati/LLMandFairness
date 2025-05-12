import numpy as np
import pandas as pd

NaN = np.nan
def is_numeric_type(column):
    return pd.api.types.is_numeric_dtype(column)

def remove_whitespaces(dataset):
    ds = dataset.copy()
    for column in dataset.columns:
        if(dataset[column].dtype == 'object'):
            ds[column] = ds[column].str.strip()
    return ds

def replaceMissingValues(dataset, values_to_searching_for):
    ds = dataset.replace(values_to_searching_for, NaN)
    return ds

def has_missing_values(dataset):
    return dataset.isna()

def handleMissingValues(dataset, handler):
    return handler(dataset)

def dropMissingValues(dataset):
    return dataset.dropna()

def removeMissingValuesHandler(dataset):
    return dataset.dropna()

def imputeMissingValues(dataset, imputer):
    return imputer(dataset)

def meanValueImputer(dataset):
    ds = dataset.copy()
    for column in dataset.columns:
        if is_numeric_type(dataset[column]):
            mean = dataset[column].mean()
            ds[column] = ds[column].fillna(mean)
    return ds