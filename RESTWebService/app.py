from flask import Flask
import flask.scaffold

flask.helpers._endpoint_from_view_func = flask.scaffold._endpoint_from_view_func
from flask_restful import Api, Resource, reqparse

import joblib
import numpy as np

app = Flask(__name__)
api = Api(app)


woz_get_args = reqparse.RequestParser()
woz_get_args.add_argument(
    "m2", type=int, required=True, help="average size of a house in m2"
)
woz_get_args.add_argument(
    "single", type=int, required=True, help="number of single households is required"
)
woz_get_args.add_argument(
    "married_nokids",
    type=int,
    required=True,
    help="number of married, no kids households is required",
)
woz_get_args.add_argument(
    "notmarried_nokids",
    type=int,
    required=True,
    help="number of not married, no kids households is required",
)
woz_get_args.add_argument(
    "married_kids",
    type=int,
    required=True,
    help="number of married, kids households is required",
)
woz_get_args.add_argument(
    "notmarried_kids",
    type=int,
    required=True,
    help="number of not married, kids households is required",
)
woz_get_args.add_argument(
    "single_parent",
    type=int,
    required=True,
    help="number of single parent households is required",
)
woz_get_args.add_argument(
    "total", type=int, required=True, help="total number of households is required"
)


class WOZ(Resource):
    def get(self):
        args = woz_get_args.parse_args()
        model_input = np.array(list(args.values())).reshape(1, -1)
        regressor = joblib.load("trained_model.sav")
        model_output = regressor.predict(model_input)
        return {"woz value": model_output[0]}


api.add_resource(WOZ, "/woz/")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
