from flask import Flask
from flask_restful import Api

from resources.trip_request import TripRequest, TripRequests

app = Flask(__name__)
api = Api(app)

api.add_resource(TripRequests, '/trip_requests/', methods=['POST', 'GET'])
api.add_resource(TripRequest, '/trip_requests/<string:trip_id>', methods=['GET', 'PUT', 'DELETE'])

app.run(host='0.0.0.0', port=5000, debug=True)
# In the context of servers, 0.0.0.0 can mean "all IPv4 addresses on the local machine".
