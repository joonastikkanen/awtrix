import src.nameday
import datetime
import yaml

# LOAD CONFIG FILE
def load_config():
    with open('./config.yaml', 'r') as file:
        config = yaml.safe_load(file)
    return config

# Set variables from config file
config = load_config()
nameday_csv_path = config['nameday_csv_path']

def get_nameday(nameday_csv_path):
    # Set day and month variables
    now = datetime.datetime.now()
    day = now.strftime("%d")
    month = now.strftime("%m")
    file_path = nameday_csv_path
    nameday = src.nameday.find_nameday(file_path, day, month)
    print(nameday)
    return nameday

get_nameday()