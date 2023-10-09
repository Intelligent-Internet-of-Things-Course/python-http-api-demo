from model.device_model import DeviceModel
import json


class DeviceUpdateRequest:

    def __init__(self, uuid, name, device_type, manufacturer, software_version, latitude, longitude):
        self.uuid = uuid
        self.name = name
        self.type = device_type
        self.manufacturer = manufacturer
        self.software_version = software_version
        self.latitude = latitude
        self.longitude = longitude

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__)
