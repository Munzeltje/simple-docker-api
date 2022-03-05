import argparse
from statistics import mean, stdev

import numpy as np
from sklearn.ensemble import RandomForestRegressor

parser = argparse.ArgumentParser()
parser.add_argument(
    "-i", type=int, default=20, help="number of iterations that are done, default: 20"
)
args = parser.parse_args()

x_train = np.load("data/x_train.npy")
x_test = np.load("data/x_test.npy")
y_train = np.load("data/y_train.npy")
y_test = np.load("data/y_test.npy")

# train and evaluate i random forests, then average their scores
scores = []
for _ in range(args.i):
    regressor = RandomForestRegressor()
    regressor.fit(x_train, y_train)
    # print(regressor.score(x_train, y_train))  # uncomment to print scores on train data
    # print(x_test[:5])                         # uncomment to see a few of the
    # print(y_test[:5])                         #   true data points and labels
    # print(regressor.predict(x_test[:5]))      # uncomment to see predicted labels
    score = regressor.score(x_test, y_test)
    scores.append(score)
print(mean(scores))
print(stdev(scores))
