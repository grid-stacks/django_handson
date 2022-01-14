import datetime
from random import randint

from django.http import HttpResponse

from channel_test.mqtt import client
from django_handson.tasks import get_users_count


def run_task(request):
    task_result = get_users_count.delay()
    print("l10", task_result)

    client.publish("test", f"{randint(10, 99)} kg")

    now = datetime.datetime.now()
    html = "<html><body>It is now %s. Celery task called.</body></html>" % now
    return HttpResponse(html)
