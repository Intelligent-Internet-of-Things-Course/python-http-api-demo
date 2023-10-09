import json
from json import JSONDecodeError
from flask import request, Response
from flask_restful import Resource, reqparse
from dto.device_creation_request import DeviceCreationRequest
from model.device_model import DeviceModel


class DevicesResource(Resource):

    def __init__(self, **kwargs):
        self.data_manager = kwargs['data_manager']

    def post(self, location_id):
        try:
            # Check if the location is correct
            if location_id in self.data_manager.location_dictionary:

                # Retrieve Location through its location_id
                target_location = self.data_manager.location_dictionary[location_id]

                # The boolean flag force the parsing of POST data as JSON irrespective of the mimetype
                json_data = request.get_json(force=True)
                device_creation_request = DeviceCreationRequest(**json_data)

                # Check if the device is new or if it already exists
                if device_creation_request.uuid in target_location.device_dictionary:
                    return {'error': "Device UUID already exists"}, 409  # return data and 200 OK code
                else:

                    # Create a new DeviceModel from the data available in the request
                    new_device_model = DeviceModel(device_creation_request.uuid,
                                                   device_creation_request.name,
                                                   location_id,
                                                   device_creation_request.type,
                                                   device_creation_request.manufacturer,
                                                   device_creation_request.software_version,
                                                   device_creation_request.latitude,
                                                   device_creation_request.longitude)

                    self.data_manager.add_device(location_id, new_device_model)
                    return Response(status=201, headers={"Location": request.url+"/"+new_device_model.uuid})  # Force the No-Content Response
            else:
                return {'error': "Location Not Found !"}, 404
        except JSONDecodeError:
            return {'error': "Invalid JSON ! Check the request"}, 400
        except Exception as e:
            return {'error': "Generic Internal Server Error ! Reason: " + str(e)}, 500

    def get(self, location_id):

        # Check if the provided Location Id in the path is correct
        if location_id in self.data_manager.location_dictionary:

            # Check for query arguments
            parser = reqparse.RequestParser()
            parser.add_argument('type', location='args')

            # Use required=True to force the check for a specific field
            # parser.add_argument('locationId', location='args', required=True)
            args = parser.parse_args()

            # Retrieve filter values
            type_filter = None
            if "type" in args:
                type_filter = args["type"]

            # Retrieve Location through its location_id
            target_location = self.data_manager.location_dictionary[location_id]

            # Iterate over the dictionary to build a serializable device list
            device_list = []
            for device in target_location.device_dictionary.values():
                device_list.append(device.__dict__)

            return device_list, 200  # return data and 200 OK code

        else:
            return {'error': "Location Not Found !"}, 404
