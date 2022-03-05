import numpy as np
import pandas as pd

def convert_to_float(series):
    """
    Takes a pandas.Series object as input and converts it to dtype float, handling NaN values.
    """
    series = series.replace(".", np.NaN)
    series = series.replace("-", np.NaN)
    series.astype(float)
    return series

def read_excel_files():
    """
    Reads the provided files and returns the data as a single pandas DataFrame.
    """
    df_prices = pd.read_excel(
        "data/woz_prices_2015_amsterdam.xlsx",
        names=["area", "average woz", "woz per m2"],
        skiprows=3,
    )[:-2]

    df_composition = pd.read_excel(
        "data/family_composition_2016_amsterdam.xlsx",
        names=[
            "area",
            "single",
            "married, no kids",
            "not married, no kids",
            "married, with kids",
            "not married, with kids",
            "single parent",
            "other",
            "total",
        ],
        skiprows=3,
    )[:-2]

    # merge dataframes and convert all columns except "area" to float
    df_combined = pd.merge(df_prices, df_composition, on="area")
    df_combined[df_combined.columns[1:]] = df_combined[df_combined.columns[1:]].apply(
        convert_to_float
    )

    return df_combined
