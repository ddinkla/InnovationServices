from flask_restful import Resource, reqparse
from flask import request

# dummy data
driverRecords = [
    {
        "name": "Iwan",
        "rating": 4.1,
        "ratingHistory": [
            3,5,4,3,5,5,4
        ],
        "id": "18CW89Q",
    },
    {
        "name": "Amber",
        "rating": 2.0,
        "ratingHistory": [
          1,2,3
        ],
        "id": "BVVX003",
    },
    {
        "name": "Kees",
        "rating": 4.2,
        "ratingHistory": [
            2,5,5,5,4
        ],
        "id": "287RTQ3",
    },
    {
        "name": "Eva",
        "rating": 4.5,
        "ratingHistory": [
            1,5,8,6,3,2,6,2,4,3,8,6
        ],
        "id": "17ER5Q",
    },
    {
        "name": "Daan",
        "rating": 5.75,
        "ratingHistory": [
            7,5,8,3
        ],
        "id": "A72TW6Q",
    },
    {
        "name": "Fabian",
        "rating": 5.54,
        "ratingHistory": [
            2,6,7,2,5,6,9,5,6,7,6
        ],
        "id": "PE126Qw",
    },
    {
        "name": "Maaike",
        "rating": 5.0,
        "ratingHistory": [
            2,7,5,6
        ],
        "id": "ER71AQ1",
    }

]

class RateDriver(Resource):

    def put(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument('rating', type=int, help='Rating given to this driver')
        args = parser.parse_args(strict=True)

        for record in driverRecords:
            if name == record["name"]:
                record['ratingHistory'].append(args["rating"])
                record["rating"] = sum(record["ratingHistory"])/len(record["ratingHistory"])
                return record, 200

        return {"message": "Driver record not found"}, 404

    def get(self, name):
        for record in driverRecords:
            if name == record["name"]:
                return {"rating": record["rating"]}, 200  # return 200 HTTP status code to indicate success
        return {"message": "Driver record not found"}, 404 # return 404 HTTP status code to indicate resource not found

class DriverRatings(Resource):
    def get(self):
        r = []
        n = []
        for record in driverRecords:
            n.append(record["id"])
            r.append(record["rating"])

        d = dict(zip(n,r))

        return d, 200

