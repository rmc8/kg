import pandas as pd
import numpy as np


def missing_data(data: pd.DataFrame) -> pd.DataFrame:
    total = data.isnull().sum()
    percent = data.isnull().sum() / data.isnull().count() * 100
    tt = pd.concat([total, percent], axis=1, keys=["Total", "Percent"])
    types: list[str] = []
    for col in data.columns:
        dtype = str(data[col].dtype)
        types.append(dtype)
    tt["Types"] = types
    return np.transpose(tt)


def most_frequent_values(data: pd.DataFrame) -> pd.DataFrame:
    total = data.count()
    tt = pd.DataFrame(total)
    tt.columns = ["Total"]
    uniques: list[int] = []
    for col in data.columns:
        unique = data[col].nunique()
        uniques.append(unique)
    tt["Uniques"] = uniques
    return np.transpose(tt)


def unique_values(data: pd.DataFrame) -> pd.DataFrame:
    total = data.count()
    tt = pd.DataFrame(total)
    tt.columns = ["Total"]
    uniques: list[int] = []
    for col in data.columns:
        unique = data[col].nunique()
        uniques.append(unique)
    tt["Uniques"] = uniques
    return np.transpose(tt)
