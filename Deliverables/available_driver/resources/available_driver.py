from flask_restful import Resource, reqparse
from flask import request
import random

best_driver = []


class AvailableDrivers(Resource):
    def post(self):
        drivers = request.get_json(force=True)
        """
        if len(best_driver) != 0:
            return {"message": "Best driver not empty"}, 400
        else:
            available_drivers = []
            for i in range(len(drivers)):
                if drivers[i]['status'] == "available":
                    available_drivers.append(drivers[i])

            
        """
        best_driver.append(random.choice(drivers))
        return best_driver, 201  # 201 Created HTTP status code

    def delete(self):
        best_driver = []
        return "{} is deleted.".format(best_driver), 200

    def get(self):
        return best_driver, 200
