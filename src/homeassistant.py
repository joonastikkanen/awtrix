import requests

def get_data_from_homeassistant_api(homeassistant_api_url, homeassistant_api_token, sensor_name):
    # Define the API endpoint and credentials
    sunrise_url = homeassistant_api_url + "/" + sensor_name
    # Set the headers with the Bearer token
    headers = {
        "Authorization": f"Bearer {homeassistant_api_token}"
    }
    # Send a GET request to the API with basic authentication
    response = requests.get(sunrise_url, headers=headers)
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        print(data)
    else:
        print(f"Failed to retrieve data: {response.status_code}")
    return response