from flask import Flask
from flask_restful import Api

from driver_rating.resources.driver_rating import RateDriver, DriverRatings

app = Flask(__name__)
api = Api(app)

api.add_resource(RateDriver, '/driver_rating/<string:name>', methods=['PUT', 'GET'])
api.add_resource(DriverRatings, '/driver_rating/', methods=['GET'])

app.run(host='0.0.0.0', port=5000, debug=True)
# In the context of servers, 0.0.0.0 can mean "all IPv4 addresses on the local machine".
