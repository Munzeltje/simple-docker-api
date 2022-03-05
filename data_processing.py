import argparse

import numpy as np
from sklearn.model_selection import train_test_split

from utils import read_excel_files


def handle_missing_values(df):
    """ Takes data from provided excel files and removes unnecessary columns
    'area', "other', 'woz per m2' as well as rows with missing values.

    Parameters
    ----------
    df : pandas DataFrame
        Contains all data from the provided files.

    Returns
    -------
    updated pandas DataFrame
    """
    df_new = df.drop(["area", "other"], axis=1)
    df_new.dropna(inplace=True)
    return df_new


def split_x_y(df_woz):
    """ Splits the data from the excel files into input and labels.

    Parameters
    ----------
    df_woz : pandas DataFrame
        Provided data, after missing values are handled.

    Returns
    -------
    tuple of numpy arrays
        The features of data points and their corresponding labels.

    """
    x = df_woz.drop("average woz", axis=1).to_numpy()
    y = df_woz["average woz"].to_numpy()
    return x, y


def normalize(x):
    """ Takes an array containing all features for each data points. First
    normalizes them by transforming counts of family compositions to percentages
    of total population.

    Parameters
    ----------
    x : numpy ndarray of shape (data points, features)

    Returns
    -------
    normalized numpy ndarray
    """
    average_m2 = x[:, 0]
    composition_counts = x[:, 1 : x.shape[1] - 1]
    total_counts = x[:, x.shape[1] - 1]

    def normalize_column(column):
        return np.multiply(np.divide(column, total_counts), 100)

    normalized_compositions = np.apply_along_axis(
        normalize_column, 0, composition_counts
    )
    normalized_compositions = np.hstack(
        (average_m2.reshape(-1, 1), normalized_compositions, total_counts.reshape(-1, 1))
    )
    return normalized_compositions


def main():
    df_woz = read_excel_files()
    df_woz = handle_missing_values(df_woz)
    df_woz.insert(2, "average m2", df_woz["average woz"].divide(df_woz["woz per m2"]))
    df_woz.drop("woz per m2", axis=1, inplace=True)
    x, y = split_x_y(df_woz)
    x = normalize(x)
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=args.t)
    np.save("data/x_all.npy", x)
    np.save("data/y_all.npy", y)
    np.save("data/x_train.npy", x_train)
    np.save("data/x_test.npy", x_test)
    np.save("data/y_train.npy", y_train)
    np.save("data/y_test.npy", y_test)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-t",
        type=float,
        default=0.3,
        help="percentage of data used for test, default = 0.3",
    )
    args = parser.parse_args()
    main()
