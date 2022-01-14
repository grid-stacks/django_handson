from django.urls import path

from channel_test import consumers

websocket_urlpatterns = [
    path('ws/sync_test/', consumers.TestSyncConsumer.as_asgi()),
    path('ws/async_test/', consumers.TestAsyncConsumer.as_asgi()),
]
