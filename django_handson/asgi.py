import os

import django
from channels.layers import get_channel_layer
from channels.routing import ProtocolTypeRouter, URLRouter, ChannelNameRouter
from django.core.asgi import get_asgi_application

from channel_test.consumers import MqttConsumer
from channel_test.mqtt import TestMqttConsumer
from django_handson.routing import websocket_urlpatterns

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_handson.settings')

django.setup()

# Application
application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': URLRouter(websocket_urlpatterns),
    'mqtt': TestMqttConsumer,
    'channel': ChannelNameRouter(
        {
            "mqtt": MqttConsumer.as_asgi()
        }
    )
})

# Layers
channel_layer = get_channel_layer()
