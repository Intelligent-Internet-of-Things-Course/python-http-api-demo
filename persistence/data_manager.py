from model.device_model import DeviceModel

class DataManager:

    device_dictionary = {}

    def add_device(self, newDevice):
        if isinstance(newDevice, DeviceModel):
            self.device_dictionary[newDevice.uuid] = newDevice
        else:
            raise TypeError("Error adding new device ! Only DeviceModel are allowed !")

    def update_device(self, updatedDevice):
        if isinstance(updatedDevice, DeviceModel):
            self.device_dictionary[updatedDevice.uuid] = updatedDevice
        else:
            raise TypeError("Error updating the device  Only DeviceModel are allowed !")

    def remove_device(self, deviceUUID):
        if deviceUUID in self.device_dictionary.keys():
            del self.device_dictionary[deviceUUID]