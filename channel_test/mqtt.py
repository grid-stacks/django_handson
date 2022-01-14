import os

import paho.mqtt.client as mqtt
from django.conf import settings
from mqttasgi.consumers import MqttConsumer


class TestMqttConsumer(MqttConsumer):
    async def connect(self):
        print('connected .........................................')
        await self.subscribe('iot/testing/topic', 2)

    async def receive(self, mqtt_message):
        print('Received a message at topic:', mqtt_message['topic'])
        print('With payload', mqtt_message['payload'])
        print('And QOS:', mqtt_message['qos'])
        pass

    async def disconnect(self):
        await self.unsubscribe('iot/testing/topic')


# The callback for when the client receives a CONNACK response from the server.
def on_connect(c, userdata, flags, rc):
    print("Connected with result code " + str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    c.subscribe("test/#")


# The callback for when a PUBLISH message is received from the server.
def on_message(c, userdata, msg):
    print(msg.topic + " " + str(msg.payload))


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_handson.settings')

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.username_pw_set(settings.MQTT_USERNAME, password=settings.MQTT_PASSWORD)
client.connect(settings.MQTT_HOST, int(settings.MQTT_PORT), 60)
