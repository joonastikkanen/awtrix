# API Docs: https://blueforcer.github.io/awtrix3/#/api
import src.mqtt_message
import src.nameday
import src.date
import src.sun
import src.nordpool
import src.weather
import yaml

# LOAD CONFIG FILE
def load_config():
    with open('./config.yaml', 'r') as file:
        config = yaml.safe_load(file)
    return config

# Set variables from config file
config = load_config()
broker_address = config['broker_address']
user = config['user']
password = config['password']
homeassistant_api_url = config['homeassistant_api_url']
homeassistant_api_token = config['homeassistant_api_token']

src.mqtt_message.send_mqtt_clear_display(broker_address, user=user, password=password)
#src.date.send_date(broker_address, topic="awtrix_1e7e38/custom/date", user=user, password=password)
src.nameday.send_nameday_message(broker_address, topic="awtrix_1e7e38/custom/nameday", user=user, password=password)
src.sun.send_sunrise(broker_address, topic="awtrix_1e7e38/custom/sunrise", user=user, password=password, homeassistant_api_url=homeassistant_api_url, homeassistant_api_token=homeassistant_api_token)
src.sun.send_sunset(broker_address, topic="awtrix_1e7e38/custom/sunset", user=user, password=password, homeassistant_api_url=homeassistant_api_url, homeassistant_api_token=homeassistant_api_token)
src.nordpool.send_nordpool(broker_address, topic="awtrix_1e7e38/custom/nordpool", user=user, password=password, homeassistant_api_url=homeassistant_api_url, homeassistant_api_token=homeassistant_api_token)
#src.weather.send_weather(broker_address, topic="awtrix_1e7e38/custom/weather", user=user, password=password, homeassistant_api_url=homeassistant_api_url, homeassistant_api_token=homeassistant_api_token)