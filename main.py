# API Docs: https://blueforcer.github.io/awtrix3/#/api
import paho.mqtt.client as mqtt
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
broker_address = "10.20.30.30"
topic = "awtrix_1e7e38/custom/hello_world"
message = {"draw":[  
 {"dc": [28, 4, 3, "#FF0000"]},  
 {"dr": [15, 4, 4, 4, "#0000FF"]},  
 {"dt": [0, 0, "Hello", "#00FF00"]}  
]}  


def send_mqtt_message(broker_address, topic, message, username=None, password=None):
    logging.info("Creating MQTT client")
    client = mqtt.Client()
    
    if username and password:
        logging.info("Setting username and password")
        client.username_pw_set(username, password)
    
    logging.info(f"Connecting to broker at {broker_address}")
    client.connect(broker_address)

    logging.info(f"Clear the display")
    client.publish("awtrix_1e7e38/custom/", "")

    logging.info(f"Publishing message to topic {topic}")
    client.publish(topic, message)
    
    logging.info("Disconnecting from broker")
    client.disconnect()

# Example usage with logging
send_mqtt_message(broker_address=str(broker_address), topic=str(topic), message=str(message), username="mqttuser", password="mummo123")