import json


class LocationCreationRequest:

    def __init__(self, uuid, name, latitude, longitude):
        self.uuid = uuid
        self.name = name
        self.latitude = latitude
        self.longitude = longitude

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__)
