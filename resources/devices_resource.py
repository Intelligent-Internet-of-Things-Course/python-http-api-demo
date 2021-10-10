import json
from json import JSONDecodeError
from flask import request, Response
from flask_restful import Resource, reqparse
from dto.device_creation_request import DeviceCreationRequest
from model.device_model import DeviceModel

class DevicesResource(Resource):

    def __init__(self, **kwargs):
        self.dataManager = kwargs['data_manager']

    def post(self):
        try:
            # The boolean flag force the parsing of POST data as JSON irrespective of the mimetype
            json_data = request.get_json(force=True)
            deviceCreationRequest = DeviceCreationRequest(**json_data)
            if deviceCreationRequest.uuid in self.dataManager.device_dictionary:
                return {'error': "Device UUID already exists"}, 409  # return data and 200 OK code
            else:
                newDeviceModel = DeviceModel.from_creation_dto(deviceCreationRequest)
                self.dataManager.add_device(newDeviceModel)
                return Response(status=201, headers={"Location": request.url+"/"+newDeviceModel.uuid})  # Force the No-Content Response
        except JSONDecodeError:
            return {'error': "Invalid JSON ! Check the request"}, 400
        except Exception as e:
            return {'error': "Generic Internal Server Error ! Reason: " + str(e)}, 500

    def get(self):

        # Check for query arguments
        parser = reqparse.RequestParser()
        parser.add_argument('type', location='args')
        parser.add_argument('locationId', location='args')
        # Use required=True to force the check for a specific field
        # parser.add_argument('locationId', location='args', required=True)
        args = parser.parse_args()

        typeFiler = args["type"]
        locationIdFilder = args["locationId"]

        print(typeFiler)
        print(locationIdFilder)

        # Iterate over the dictionary to build a serializable device list
        device_list = []
        for device in self.dataManager.device_dictionary.values():
            device_list.append(device.__dict__)
        return device_list, 200  # return data and 200 OK code