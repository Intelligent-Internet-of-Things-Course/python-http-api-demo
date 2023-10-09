import requests

import requests

target_location_id = "l0001"

# Target API URL
api_url = f'http://127.0.0.1:7070/api/iot/inventory/location/{target_location_id}'

# Define Update Request Body as Python dictionary
request_dictionary = {
    "uuid": target_location_id,
    "name": "PythonUpdated-TestBuilding",
    "latitude": 48.412321,
    "longitude": 10.533423211
}

# Send the PUT Request with the body serialized as Json (Internally managed by the library)
response = requests.put(api_url, json=request_dictionary)

print(f'HTTP Response Code: {response.status_code} - Buffer Body: {response.content}')