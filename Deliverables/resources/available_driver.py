from flask_restful import Resource, reqparse
from flask import request
import random

best_driver = []


class DriverLocation(Resource):
    def get(self, driver_id):
        for driver in driver_locations:
            if driver_id == driver["driver_id"]:
                return driver, 200  # return 200 HTTP status code to indicate success
        return {"message": "Driver not found"}, 404  # return 404 HTTP status code to indicate resource not found



class AvailableDrivers(Resource):
    def post(self):
        drivers = request.get_json(force=True)

        if len(best_driver) != 0:
            return {"message": "Best driver not empty"}, 400

        available_drivers = []
        for i in range(len(drivers)):
            if drivers[i]['status'] == "available":
                available_drivers.append(drivers[i])

        best_driver.append(random.choice(available_drivers))
        return best_driver, 201  # 201 Created HTTP status code

    def delete(self):
        best_driver = []
        return "{} is deleted.".format(best_driver), 200

    def get(self):
        return best_driver, 200