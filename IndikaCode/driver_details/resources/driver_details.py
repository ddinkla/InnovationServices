from flask_restful import Resource, reqparse
from flask import request

# dummy data
drivers = [
    {
        "driver_id": "d12542",
        "name": "Fernando Alonso",
        "status": "offline",
        "CarType": "basic"
    },
    {
        "driver_id": "d85719",
        "name": "Daniel Ricciardo",
        "status": "available",
        "CarType": "basic"
    },
    {
        "driver_id": "d54818",
        "name": "Lewis Hamilton",
        "status": "driving",
        "CarType": "premium"
    },
    {
        "driver_id": "d762057",
        "name": "Max Verstappen",
        "status": "available",
        "CarType": "premium"
    }
]


# resource place record
class DriverRecord(Resource):
    def get(self, driver_id):
        for driver in drivers:
            if driver_id == driver["driver_id"]:
                return driver, 200  # return 200 HTTP status code to indicate success
        return {"message": "Driver not found"}, 404  # return 404 HTTP status code to indicate resource not found

    def put(self, driver_id):
        parser = reqparse.RequestParser()
        parser.add_argument("status", type=str, help="Status not valid, change driver status",
                            choices=['available', 'driving', 'offline'])
        args = parser.parse_args(strict=True)

        # possible_status = ['available', 'driving', 'offline']
        # if args["Status"] not in possible_status:
        #    return {"message": "Bad request, status not in status format (available, driving, offline)"}, 400
        # else:

        for driver in drivers:
            if driver_id == driver["driver_id"]:
                driver["status"] = args["status"]
                return driver, 200

        return {"message": "Trip not found"}, 404

    def delete(self, driver_id):
        to_be_deleted = None
        for driver in drivers:
            if driver_id == driver["driver_id"]:
                to_be_deleted = driver
                break

        if to_be_deleted:
            drivers.remove(to_be_deleted)
            return "{} is deleted.".format(driver_id), 200
        return {"message": "Driver not found"}, 404


# resource collection Drivers
class DriverRecords(Resource):
    def post(self):
        driver_to_be_created = request.get_json(force=True)
        driver_id = driver_to_be_created["driver_id"]
        for driver in drivers:
            if driver_id == driver["driver_id"]:
                # 500 Internal Server Error HTTP status code
                return {"message": "Driver with ID {} already exists".format(driver_id)}, 500

        drivers.append(driver_to_be_created)
        return driver_to_be_created, 201  # 201 Created HTTP status code

    def get(self):
            return drivers, 200
