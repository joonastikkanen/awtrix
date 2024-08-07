# API Docs: https://blueforcer.github.io/awtrix3/#/api
import paho.mqtt.client as mqtt
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
broker_address = "10.20.30.30"
topic = "awtrix_1e7e38/rtttl"
# Load the contents of the text file into the message variable
with open("./rtttl/Films And Tv - Robocop.txt", "r") as file:
    message = "rttl " + file.read()


def send_mqtt_message(broker_address, topic, message, username=None, password=None):
    logging.info("Creating MQTT client")
    client = mqtt.Client()
    
    if username and password:
        logging.info("Setting username and password")
        client.username_pw_set(username, password)
    
    logging.info(f"Connecting to broker at {broker_address}")
    client.connect(broker_address)

    logging.info(f"Publishing message to topic {topic}")
    client.publish(topic, message)
    
    logging.info("Disconnecting from broker")
    client.disconnect()

# Example usage with logging
send_mqtt_message(broker_address=str(broker_address), topic=str(topic), message=str(message), username="mqttuser", password="mummo123")