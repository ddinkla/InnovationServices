from flask import Flask
from flask_restful import Api

from resources.trip_request import TripRequest, TripRequests, TripsRequests
from resources.drivers import DriverRecord, DriverRecords, DriversRecords

app = Flask(__name__)
api = Api(app)

api.add_resource(TripRequests, '/trip_requests/', methods=['POST'])
api.add_resource(TripRequest, '/trip_requests/<string:trip_id>', methods=['GET', 'PUT', 'DELETE'])
api.add_resource(TripsRequests, '/trip_requests/', methods=['GET'])

api.add_resource(DriverRecords, '/drivers/', methods=['POST'])
api.add_resource(DriverRecord, '/drivers/<string:driver_id>', methods=['GET', 'PUT', 'DELETE'])
api.add_resource(DriversRecords, '/drivers/', methods=['GET'])

app.run(host='0.0.0.0', port=5000, debug=True)
# In the context of servers, 0.0.0.0 can mean "all IPv4 addresses on the local machine".
