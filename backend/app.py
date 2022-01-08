from flask import Flask, request
from flask_restful import Api, Resource
from flask_cors import CORS
import pandas as pd

from Algorithm import main_logic

app = Flask(__name__)
CORS(app)
api = Api(app)

pref_map = {
        1: "Cinema",
        2: "Library",
        3: "No Preference",
        4: "Museum"
    }

data = pd.read_csv("./data.csv")

class MeetingPoints(Resource):
    def get(self, pref_id):
        query_params = request.args.to_dict(flat=False)
        output = main_logic(query_params["start"], pref_map[pref_id])
        final_output = list(
            map(
                lambda z: {
                    "name": z,
                    "things": [
                        data[data['Name'] == z].iloc[0]['Item_one'],
                        data[data['Name'] == z].iloc[0]['Item_two'],
                        data[data['Name'] == z].iloc[0]['item_three']
                    ]
                }, output))
        return {"data": final_output}


api.add_resource(MeetingPoints, "/api/<int:pref_id>")

if __name__ == '__main__':
    app.run(debug=True)
