from json import JSONDecodeError
from flask import request, Response
from flask_restful import Resource
from dto.device_creation_request import DeviceCreationRequest


class DeviceResource(Resource):

    def __init__(self, **kwargs):
        self.dataManager = kwargs['data_manager']

    def get(self, device_id):
        print(device_id)
        return {'device-uuid': device_id}, 200  # return data and 200 OK code

    def delete(self, device_id):
        try:
            if device_id in self.dataManager.device_dictionary:
               self.dataManager.remove_device(device_id)
               return Response(status=204)
            else:
                return {'error': "Device UUID not found"}, 404
        except Exception as e:
            return {'error': "Generic Internal Server Error ! Reason: " + str(e)}, 500

    def put(self, device_id):
        try:
            if device_id in self.dataManager.device_dictionary:
                # The boolean flag force the parsing of POST data as JSON irrespective of the mimetype
                json_data = request.get_json(force=True)
                deviceCreationRequest = DeviceCreationRequest(**json_data)
                if deviceCreationRequest.uuid != device_id:
                    return {'error': "UUID mismatch between body and resource"}, 400  # return data and 200 OK code
                else:
                    self.dataManager.update_device(deviceCreationRequest)
                    return Response(status=204)
            else:
                return {'error': "Device UUID not found"}, 404
        except JSONDecodeError:
            return {'error': "Invalid JSON ! Check the request"}, 400
        except Exception as e:
            return {'error': "Generic Internal Server Error ! Reason: " + str(e)}, 500
