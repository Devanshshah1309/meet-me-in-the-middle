from flask import Flask, request
from flask_restful import Api, Resource

from Algorithm import main_logic

app = Flask(__name__)
api = Api(app)


class MeetingPoints(Resource):
    def get(self):
        query_params = request.args.to_dict(flat=False)
        output = main_logic(query_params["start"])
        return {"data": output}


api.add_resource(MeetingPoints, "/api")

if __name__ == '__main__':
    app.run(debug=True)
