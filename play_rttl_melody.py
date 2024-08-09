import src.mqtt_message
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

melody_folder = './files/rtttl/'
melody_file = 'Boomfunk MC - Freestyler.txt'
melody_path = melody_folder + melody_file

# Function to read file content
def read_file_content(melody_path):
    with open(melody_path, 'r') as file:
        return file.read()

melody = read_file_content(melody_path)
message = "rttl %s" % melody
topic = "awtrix_1e7e38/rtttl"

src.mqtt_message.send_mqtt_message(broker_address=str(broker_address), topic=str(topic), message=str(message), user=user, password=password)