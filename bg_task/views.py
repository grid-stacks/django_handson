import datetime

from django.http import HttpResponse

from channel_test.tasks import mqtt_pub_test
from django_handson.tasks import get_users_count


def run_task(request):
    task_result = get_users_count.delay()
    mqtt_result = mqtt_pub_test.delay(msg="Wow")
    print("l12", task_result)
    print("l13", mqtt_result)

    now = datetime.datetime.now()
    html = "<html><body>It is now %s. Celery task called.</body></html>" % now
    return HttpResponse(html)
