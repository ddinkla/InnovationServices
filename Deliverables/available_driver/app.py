from flask import Flask
from flask_restful import Api

from available_driver.resources.available_driver import AvailableDrivers

app = Flask(__name__)
api = Api(app)

api.add_resource(AvailableDrivers, '/available_driver/', methods=['POST', 'DELETE', 'GET'])

app.run(host='0.0.0.0', port=5000, debug=True)
# In the context of servers, 0.0.0.0 can mean "all IPv4 addresses on the local machine".
