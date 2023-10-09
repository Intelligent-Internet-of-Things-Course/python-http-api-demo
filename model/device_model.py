import json


class DeviceModel:

    DEVICE_TYPE_DEFAULT = "device.default"
    DEVICE_TYPE_MOBILE = "device.mobile"
    DEVICE_TYPE_SENSOR = "device.sensor"
    DEVICE_TYPE_ACTUATOR = "device.actuator"

    def __init__(self, uuid, name, location_id, device_type, manufacturer, software_version, latitude, longitude):
        self.uuid = uuid
        self.name = name
        self.locationId = location_id
        self.type = device_type
        self.manufacturer = manufacturer
        self.software_version = software_version
        self.latitude = latitude
        self.longitude = longitude

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__)
