import argparse

import numpy as np
from matplotlib import pyplot as plt

from utils import read_excel_files


parser = argparse.ArgumentParser()
parser.add_argument('-p', type=int, default=0,
                    help="set to 1 for analyzing data after processing, default: 0")
args = parser.parse_args()

# analyze data before it is processed
if args.p == 0:
    df_woz = read_excel_files()

    # check dtypes and make statistical summary
    with open("out/data_analysis.txt", "w") as file:
        file.write(df_woz.dtypes.to_string())
        file.write("\n\n")
        file.write(df_woz.describe().to_string())
        file.write("\n\n")
        file.write(df_woz.isna().sum().to_string())

# analyze data after it is processed
else:
    data = np.load("data/x_all.npy")
    features = [
        "average m2",
        "single",
        "married, no kids",
        "not married, no kids",
        "married, with kids",
        "not married, with kids",
        "single parent",
        "total"
    ]
    with open("out/data_analysis_after_processing.txt", "w") as file:
        file.write("")
    plt.rcParams.update({'font.size': 18})
    for i in range(data.shape[1]):
        with open("out/data_analysis_after_processing.txt", "a") as file:
            file.write(features[i] +":\n")
            file.write("min - max: {0} - {1}\n".format(np.min(data[:, i]), np.max(data[:, i])))
            file.write("mean: {0} \n".format(np.mean(data[:, i])))
            file.write("SD: {0} \n\n".format(np.std(data[:, i])))
        _ = plt.hist(data[:, i], bins=20)
        plt.savefig('out/hist{0}.png'.format(i))
        plt.clf()
    _ = plt.hist(data[:, 7][:-1], bins=20)
    plt.savefig('out/hist7_no_outlier.png')
