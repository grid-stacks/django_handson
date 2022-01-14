from django.urls import path

from channel_test import consumers
from channel_test.mqtt import TestMqttConsumer

websocket_urlpatterns = [
    path('ws/sync_test/', consumers.TestSyncConsumer.as_asgi()),
    path('ws/async_test/', consumers.TestAsyncConsumer.as_asgi()),
    path("ws/mqtt.sub/", TestMqttConsumer.as_asgi()),
]
