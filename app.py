from flask import Flask
from flask_restful import Resource, Api

from api.utils import countries

app = Flask(__name__)
api = Api(app)

class Countries(Resource):
    def get(self):
        return countries().to_json()

api.add_resource(Countries , '/')

if __name__ == '__main__':
    app.run(debug=True)