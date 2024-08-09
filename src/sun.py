import src.mqtt_message
import src.homeassistant
import datetime
import requests
import pytz

def send_sunrise(broker_address, topic, user, password, homeassistant_api_url, homeassistant_api_token):
    sunrise_response = src.homeassistant.get_data_from_homeassistant_api(homeassistant_api_url, homeassistant_api_token, "sensor.sun_next_rising")
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
        "icon": "44904",
        "text": "%s" % time_only
        }
    
    src.mqtt_message.send_mqtt_message(broker_address=str(broker_address), topic=str(topic), message=str(message), user=user, password=password)
    return True

def send_sunset(broker_address, topic, user, password, homeassistant_api_url, homeassistant_api_token):
    sunset_response = src.homeassistant.get_data_from_homeassistant_api(homeassistant_api_url, homeassistant_api_token, "sensor.sun_next_setting")
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
        "icon": "44905",
        "text": "%s" % time_only
        }
    
    src.mqtt_message.send_mqtt_message(broker_address=str(broker_address), topic=str(topic), message=str(message), user=user, password=password)
    return True
    