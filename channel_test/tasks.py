from __future__ import absolute_import, unicode_literals

from asgiref.sync import async_to_sync
from celery import shared_task
from channels.layers import get_channel_layer

channel_layer = get_channel_layer()


@shared_task(bind=True)
def mqtt_pub_test(self, msg):
    # print(dir(self))
    print(f"Celery task say: {self.request.id}")

    async_to_sync(channel_layer.send)('default', {
        'type': 'mqtt.pub',
        'text': {
            'topic': 'test',
            'payload': f"Great - {msg}"
        }
    })

    return msg
