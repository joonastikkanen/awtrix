import src.mqtt_message
import csv
import datetime

def find_nameday(file_path, day, month):
    with open(file_path, mode='r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            # Assuming the day is in the first column and the month is in the second column
            row_monthday = row[0]
            if row_monthday == "%s-%s" % (month, day):
                return row[1]
    return None

def send_nameday_message(broker_address, topic, user, password):
    # Set day and month variables
    now = datetime.datetime.now()
    day = now.strftime("%d")
    month = now.strftime("%m")
    file_path = './files/namedays.csv'
    nameday = find_nameday(file_path, day, month)
    message = {
        "text": [
            {
                "t": "Nimipäivä tänään: ",
                "c": "FFFFFF",
            },
            {
                "t": "%s" % nameday,
                "c": "00FF00",
            }
        ],
        "repeat": 3
        }
    src.mqtt_message.send_mqtt_message(broker_address=str(broker_address), topic=str(topic), message=str(message), user=user, password=password)
    return True