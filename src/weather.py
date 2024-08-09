import src.mqtt_message
import src.homeassistant

def send_weather(broker_address, topic, user, password, homeassistant_api_url, homeassistant_api_token):
    condition_response = src.homeassistant.get_data_from_homeassistant_api(homeassistant_api_url, homeassistant_api_token, "sensor.koti_condition_day_0")
    today_max_response = src.homeassistant.get_data_from_homeassistant_api(homeassistant_api_url, homeassistant_api_token, "sensor.koti_realfeel_temperature_max_day_0")
    today_min_response = src.homeassistant.get_data_from_homeassistant_api(homeassistant_api_url, homeassistant_api_token, "sensor.koti_realfeel_temperature_min_day_0")
    message = {
        "text": "Weather today: %s, Max Temp.: %s °C, Min Temp.: %s °C" % (condition_response.json().get("state"), today_max_response.json().get("state"), today_min_response.json().get("state")),
        "repeat": 3,
        "scrollSpeed": 80
        }
    src.mqtt_message.send_mqtt_message(broker_address=str(broker_address), topic=str(topic), message=str(message), user=user, password=password)
    return True    
    