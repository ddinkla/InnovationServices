from flask import Flask
from flask_restful import Api

from driver_location.resources.driver_location import DriverLocation, DriverLocations

app = Flask(__name__)
api = Api(app)

api.add_resource(DriverLocation, '/driver_locations/<string:driver_id>', methods=['GET', 'PUT', 'DELETE'])
api.add_resource(DriverLocations, '/driver_locations/', methods=['POST', 'GET'])

app.run(host='0.0.0.0', port=5000, debug=True)
# In the context of servers, 0.0.0.0 can mean "all IPv4 addresses on the local machine".
