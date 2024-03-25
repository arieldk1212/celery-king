import os
from celery import Celery
from decouple import config

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "server.settings")

app = Celery("server", broker=config("CELERY_BROKER_REDIS_URL"))

app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks()