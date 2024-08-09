import src.mqtt_message
from jinja2 import Environment, FileSystemLoader
import src.homeassistant

def send_nordpool(broker_address, topic, user, password, homeassistant_api_url, homeassistant_api_token):
    # Context variables
    nordpool_response = src.homeassistant.get_data_from_homeassistant_api(homeassistant_api_url, homeassistant_api_token, "sensor.nordpool_kwh_fi_eur_3_00_024")
    nordpool_prices = nordpool_response.json()
    current_price = float(nordpool_prices.get("state"))
    hourly_attribute = nordpool_prices.get("attributes").get("today")
    nordpool_prices = hourly_attribute
    unit = "c/kWh"
    unit_multiplier = 100
    multiplied_price = current_price * unit_multiplier
    message_duration = 30
    icon = 54077
    price_text = str(multiplied_price) + unit
    # Jinja2
    template_dir = './files'  # Directory containing your template files
    env = Environment(loader=FileSystemLoader(template_dir))
    template_name = 'nordpool.json.j2'  # Replace with your template file name
    template = env.get_template(template_name)
    context = {
        "hourly_attribute": hourly_attribute,
        "unit": unit,
        "unit_multiplier": unit_multiplier,
        "message_duration": message_duration,
        "icon": icon,
        "nordpool_prices": nordpool_prices,
        "current_price": current_price,
        "multiplied_price": multiplied_price,
        "price_text": price_text
        }
    message = template.render(context)
    print(message)
    src.mqtt_message.send_mqtt_message(broker_address=str(broker_address), topic=str(topic), message=str(message), user=user, password=password)
    return True
