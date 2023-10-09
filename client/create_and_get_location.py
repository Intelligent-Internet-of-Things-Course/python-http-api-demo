import requests

import requests

# Target API URL
api_url = "http://127.0.0.1:7070/api/iot/inventory/location"

# Define Request Body as Python dictionary
request_dictionary = {
    "uuid": "l112",
    "name": "PythonTestBuilding",
    "latitude": 48.412321,
    "longitude": 10.533423211
}

response = requests.post(api_url, json=request_dictionary)
response_code = response.status_code

if response_code == 201 and "Location" in response.headers:

    location_header = response.headers["Location"]
    print(f'HTTP Response Code: {response.status_code} - Buffer Body: {response.content} - Location Header: {location_header}')

    get_api_url = location_header
    response = requests.get(get_api_url)
    json_response = response.json()

    print("Reading the new created Location Resource ...")
    print(f'HTTP Response Code: {response.status_code} - Json Parsed Body {json_response}')
else:
    print(f'Error creating the Location ! Code: {response_code} and Reason: {str(response.content, "UTF-8").strip()}')