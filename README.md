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

