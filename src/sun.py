import src.mqtt_message
import datetime
import requests
from requests.auth import HTTPBasicAuth
import pytz

def send_sunrise(broker_address, topic, user, password, homeassistant_api_url, homeassistant_api_token):
    # Set day and month variables
    # Define the API endpoint and credentials
    sunrise_url = homeassistant_api_url + "/sensor.sun_next_rising"
    # Set the headers with the Bearer token
    headers = {
        "Authorization": f"Bearer {homeassistant_api_token}"
    }
    # Send a GET request to the API with basic authentication
    sunrise_response = requests.get(sunrise_url, headers=headers)
    # Check if the request was successful
    if sunrise_response.status_code == 200:
        # Parse the JSON response
        data = sunrise_response.json()
        # Process the data as needed
        sun_rising = data.get("state")
        # Parse the datetime string
        utc_time = datetime.datetime.strptime(sun_rising, "%Y-%m-%dT%H:%M:%S%z")
        
        # Convert to the desired timezone (UTC+3)
        target_timezone = pytz.timezone("Etc/GMT-3")
        local_time = utc_time.astimezone(target_timezone)
        
        # Extract the time part
        time_only = local_time.strftime("%H:%M")
        print(time_only)
    else:
        print(f"Failed to retrieve data: {sunrise_response.status_code}")
        return False

    message = {
        "icon": "44905",
        "text": "%s" % time_only
        }
    
    src.mqtt_message.send_mqtt_message(broker_address=str(broker_address), topic=str(topic), message=str(message), user=user, password=password)
    return True

def send_sunset(broker_address, topic, user, password, homeassistant_api_url, homeassistant_api_token):
    # Set day and month variables
    # Define the API endpoint and credentials
    sunset_url = homeassistant_api_url + "/sensor.sun_next_setting"
    # Set the headers with the Bearer token
    headers = {
        "Authorization": f"Bearer {homeassistant_api_token}"
    }
    # Send a GET request to the API with basic authentication
    sunset_response = requests.get(sunset_url, headers=headers)
    # Check if the request was successful
    if sunset_response.status_code == 200:
        # Parse the JSON response
        data = sunset_response.json()
        # Process the data as needed
        sun_setting = data.get("state")
        # Parse the datetime string
        utc_time = datetime.datetime.strptime(sun_setting, "%Y-%m-%dT%H:%M:%S%z")
        
        # Convert to the desired timezone (UTC+3)
        target_timezone = pytz.timezone("Etc/GMT-3")
        local_time = utc_time.astimezone(target_timezone)
        
        # Extract the time part
        time_only = local_time.strftime("%H:%M")
        print(time_only)
    else:
        print(f"Failed to retrieve data: {sun_setting.status_code}")
        return False

    message = {
        "icon": "44904",
        "text": "%s" % time_only
        }
    
    src.mqtt_message.send_mqtt_message(broker_address=str(broker_address), topic=str(topic), message=str(message), user=user, password=password)
    return True
    