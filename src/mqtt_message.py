import paho.mqtt.client as mqtt
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def send_mqtt_message(broker_address, topic, message, user=None, password=None):
    
    logging.info("Creating MQTT client")
    client = mqtt.Client()
    
    if user and password:
        logging.info("Setting username and password")
        client.username_pw_set(user, password)
    
    logging.info(f"Connecting to broker at {broker_address}")
    client.connect(broker_address)

    logging.info(f"Publishing message to topic {topic}")
    client.publish(topic, message)
    
    logging.info("Disconnecting from broker")
    client.disconnect()

def send_mqtt_clear_display(broker_address, user=None, password=None):
    logging.info("Creating MQTT client")
    client = mqtt.Client()
    
    if user and password:
        logging.info("Setting username and password")
        client.username_pw_set(user, password)
    
    logging.info(f"Connecting to broker at {broker_address}")
    client.connect(broker_address)

    logging.info(f"Clear the display")
    client.publish("awtrix_1e7e38/custom/test", "")
    
    logging.info("Disconnecting from broker")
    client.disconnect()