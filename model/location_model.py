import json


class LocationModel:

    def __init__(self, uuid, name, latitude, longitude):
        self.uuid = uuid
        self.name = name
        self.latitude = latitude
        self.longitude = longitude
        self.device_dictionary = {}

    @staticmethod
    def from_creation_dto(location_creation_request):
        return LocationModel(location_creation_request.uuid,
                             location_creation_request.name,
                             location_creation_request.latitude,
                             location_creation_request.longitude)

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__)
