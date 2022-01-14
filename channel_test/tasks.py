from celery import shared_task

from channel_test.mqtt import client


@shared_task(bind=True)
def mqtt_pub_test(self, weight):
    print(f"Celery task say: {self.request.id}")

    client.publish("test", f"{weight} kg")

    return weight
