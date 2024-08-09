import src.mqtt_message
import datetime

def send_date(broker_address, topic, user, password):
    # Set day and month variables
    now = datetime.datetime.now()
    day = now.strftime("%d").lstrip('0')
    hour = now.strftime("%H")
    minute = now.strftime("%M")
    message = {
        "draw":[  
            {
                "dr": [0, 0, 9, 2, "#FC0808"]
            },
            {
                "df": [0, 2, 9, 6, "#FFFFFF"]
            },
            {
                "dt": [ 3 , 2, "%s" % day, "#000000"]
            },
        ],
        "text": "%s:%s" % (hour, minute),
        "textOffset": 5
        }
    src.mqtt_message.send_mqtt_message(broker_address=str(broker_address), topic=str(topic), message=str(message), user=user, password=password)
    return True
    