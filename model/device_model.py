import json


class DeviceModel:

    def __init__(self, uuid, name, locationId, type, attributes):
        self.uuid = uuid
        self.name = name
        self.locationId = locationId
        self.type = type
        self.attributes = attributes

    @staticmethod
    def from_creation_dto(deviceCreationRequest):
        return DeviceModel(deviceCreationRequest.uuid,
                           deviceCreationRequest.name,
                           deviceCreationRequest.locationId,
                           deviceCreationRequest.type,
                           deviceCreationRequest.attributes)

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__)
