import os

import paho.mqtt.client as mqtt
from django.conf import settings


# The callback for when the client receives a CONNACK response from the server.
def on_connect(c, userdata, flags, rc):
    print("Connected with result code " + str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    c.subscribe("test/#")


# The callback for when a PUBLISH message is received from the server.
def on_message(c, userdata, msg):
    print("l18 mqtt =======================================")
    print(msg.topic + " " + str(msg.payload))
    print('msg', msg)


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_handson.settings')

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.username_pw_set(settings.MQTT_USERNAME, password=settings.MQTT_PASSWORD)
client.connect(settings.MQTT_HOST, int(settings.MQTT_PORT), 60)
