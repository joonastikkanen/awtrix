# Awtrix display apps

* Nordpool homeassistant: https://flows.blueforcer.de/flow/gLB25zlMoWZp

## Configuration file config.yml

```yaml
broker_address: <IP ADDRESS>
user: <MQTT USER>
password: <MQTT USER PASSWORD>
homeassistant_api_url: <HOMEASSISTANT API URL>
homeassistant_api_token: <HOMEASSISTANT BEARER TOKEN>
```

## Send message to MQTT Broker using command line

```
$ mosquitto_pub -h <broker_address> -t <topic> -m <message> -u <username> -P <password>
```

## Nameday Homeassistant sensor

Put these lines to configuration.yml

```yaml
# Python AWTRIX nameday Display
command_line:
- sensor:
    name: AWTRIX Nameday Python Script
    command: python scripts/awtrix/nameday_ha_sensor.py scripts/awtrix/files/namedays.csv
    scan_interval: 43200 # update twice a day
```