from django.urls import path

from bg_task.views import run_task

app_name = "bg_task"
urlpatterns = [
    path("run_task", view=run_task, name="run_task"),
]
