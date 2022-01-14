import os

from celery import Celery

# set the default Django settings module for the 'celery' program.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_handson.settings")

app = Celery("handson")

# Using a string here means the worker doesn't have to serialize the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys should have a `CELERY_` prefix.
app.config_from_object("django.conf:settings", namespace="CELERY")

app.conf.beat_schedule = {
    'msg-every-60-seconds': {
        'task': 'channel_test.tasks.mqtt_pub_test',
        'schedule': 60,
        'args': ('30',)
    },
}

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()
