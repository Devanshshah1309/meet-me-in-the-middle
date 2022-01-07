from flask import Flask, request
from flask_restful import Api, Resource
from flask_cors import CORS

from Algorithm import main_logic

app = Flask(__name__)
CORS(app)
api = Api(app)

pref_map = {
        1: "Cinema",
        2: "Library",
        3: "No Preference"
    }


class MeetingPoints(Resource):
    def get(self, pref_id):
        query_params = request.args.to_dict(flat=False)
        output = main_logic(query_params["start"], pref_map[pref_id])
        return {"data": output}


api.add_resource(MeetingPoints, "/api/<int:pref_id>")

if __name__ == '__main__':
    app.run(debug=True)
