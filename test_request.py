import argparse

import requests

parser = argparse.ArgumentParser()
parser.add_argument("-m2", type=int, default=80, help="average size of house in m2")
parser.add_argument("-s", type=int, default=20, help="number of single households")
parser.add_argument(
    "-mn", type=int, default=20, help="number of married, no kids households"
)
parser.add_argument(
    "-nn", type=int, default=20, help="number of not married, no kids households"
)
parser.add_argument(
    "-mk", type=int, default=20, help="number of married, kids households"
)
parser.add_argument(
    "-nk", type=int, default=20, help="number of not married, kids households"
)
parser.add_argument(
    "-sp", type=int, default=20, help="number of single parent households"
)
args = parser.parse_args()
total = sum([args.s, args.mn, args.nn, args.mk, args.nk, args.sp])

BASE = "http://0.0.0.0:5000/"

response = requests.get(
    BASE
    + "woz/?m2={0}&single={1}&married_nokids={2}&notmarried_nokids={3}&married_kids={4}&notmarried_kids={5}&single_parent={6}&total={7}".format(
        args.m2, args.s, args.mn, args.nn, args.mk, args.nk, args.sp, total
    )
)
print(response.json())
