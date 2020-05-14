from flask_restful import Resource, reqparse
from flask import request

# dummy data
driver_locations = [
    {
        "driver_id": "d85719",
        "last_location": [51.676213, 5.289145],
    },
    {
        "driver_id": "d762057",
        "last_location": [51.71853, 5.2960],
    },
    {
        "driver_id": "d12542",
        "last_location": [52.567145, 4.86514]
    },
    {
        "driver_id": "d54818",
        "last_location": [53.07613, 6.855135]
    }
]


# resource place record
class DriverLocation(Resource):
    def get(self, driver_id):
        for driver in driver_locations:
            if driver_id == driver["driver_id"]:
                return driver, 200  # return 200 HTTP status code to indicate success
        return {"message": "Driver not found"}, 404  # return 404 HTTP status code to indicate resource not found

    def put(self, driver_id):
        parser = reqparse.RequestParser()
        parser.add_argument("last_location_lat", type=float, help="Change last location latitude")
        parser.add_argument("last_location_long", type=float, help="Change last location longitude")
        args = parser.parse_args(strict=True)

        if args["last_location_lat"] is None or args["last_location_long"] is None:
            return {"message": "Invalid location, latitude or longitude is None"}, 400

        for driver in driver_locations:
            if driver_id == driver["driver_id"]:
                driver["last_location"][0] = args["last_location_lat"]
                driver["last_location"][1] = args["last_location_long"]
                return driver, 200

        return {"message": "Place record not found"}, 404

    def delete(self, driver_id):
        to_be_deleted = None
        for driver in driver_locations:
            if driver_id == driver["driver_id"]:
                to_be_deleted = driver
                break

        if to_be_deleted:
            driver_locations.remove(to_be_deleted)
            return "{} is deleted.".format(driver_id), 200
        return {"message": "Driver not found"}, 404


# resource collection Drivers
class DriverLocations(Resource):
    def post(self):
        location_to_be_created = request.get_json(force=True)
        driver_id = location_to_be_created["driver_id"]
        for driver in driver_locations:
            if driver_id == driver["driver_id"]:
                # 500 Internal Server Error HTTP status code
                return {"message": "Driver with ID {} already exists".format(driver_id)}, 500

        driver_locations.append(location_to_be_created)
        return location_to_be_created, 201  # 201 Created HTTP status code

    def get(self):
            return driver_locations, 200

