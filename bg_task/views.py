import datetime

from django.http import HttpResponse

from django_handson.tasks import get_users_count


def run_task(request):
    task_result = get_users_count.delay()
    print("l10", task_result)

    now = datetime.datetime.now()
    html = "<html><body>It is now %s. Celery task called.</body></html>" % now
    return HttpResponse(html)
