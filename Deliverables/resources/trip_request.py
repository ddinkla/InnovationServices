from flask_restful import Resource, reqparse
from flask import request

# dummy data
trips = [
    {
        "trip_id": "31353",
        "customer_name":"Beyonce",
        "customer_id": "u314958",
        "location": "JADS, Den Bosch",
        "destination": "Eindhoven University"
    },
    {
        "trip_id": "14891",
        "customer_name": "Queen Maxima",
        "customer_id": "u035135",
        "location":  "JADS, Den Bosch",
        "destination":  "Tilburg University"  # Tilburg University
    },
    {
        "trip_id": "15183",
        "customer_name": "Michelle Obama",
        "customer_id": "u51351",
        "location":  "JADS, Den Bosch",
        "destination": "Schiphol Airport"  # Schiphol Airport Coordinates
    }
]


# resource place record
class TripRequest(Resource):
    def get(self, trip_id):
        for trip in trips:
            if trip_id == trip["trip_id"]:
                return trip, 200  # return 200 HTTP status code to indicate success
        return {"message": "Trip not found"}, 404  # return 404 HTTP status code to indicate resource not found

    def put(self, trip_id):
        parser = reqparse.RequestParser()
        parser.add_argument("destination", type=float, help="Change destination")
        args = parser.parse_args(strict=True)

        for trip in trips:
            if trip_id == trip["trip_id"]:
                trip["destination"] = args["destination"]
                return trip, 200

        return {"message": "Trip not found"}, 404

    def delete(self, trip_id):
        to_be_deleted = None
        for trip in trips:
            if trip_id == trip["trip_id"]:
                to_be_deleted = trip
                break

        if to_be_deleted:
            trips.remove(to_be_deleted)
            return "{} is deleted.".format(trip_id), 200
        return {"message": "Trip not found"}, 404


# resource collection TripRequests
class TripRequests(Resource):
    def post(self):
        trip_to_be_created = request.get_json(force=True)
        trip_id = trip_to_be_created["trip_id"]
        for trip in trips:
            if trip_id == trip["trip_id"]:
                # 500 Internal Server Error HTTP status code
                return {"message": "Trip with ID {} already exists".format(trip_id)}, 500

        trips.append(trip_to_be_created)
        return trip_to_be_created, 201  # 201 Created HTTP status code

    def get(self):
            return trips, 200
