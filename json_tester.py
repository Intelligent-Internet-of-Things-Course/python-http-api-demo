import json
from model.device_model import DeviceModel

test_json_string = '{"uuid": "device00002","name": "Demo Temperature Sensor 2","locationId": "000001","type": "dev:dummy:temperature","attributes": {"min_value": -200,"unit": "C","software_version": "0.0.1","battery": false,"manufacturer": "ACME Corporation","max_value": 200}}'

if __name__ == '__main__':
    print(test_json_string)
    desDictionary = json.loads(test_json_string)
    print(type(desDictionary))
    deviceModel = DeviceModel(**desDictionary)
    print(type(deviceModel))
    print(deviceModel.uuid)
    print(json.dumps(deviceModel.__dict__))
    print(deviceModel.to_json())

