from __future__ import absolute_import
from celery import Celery
from celery.schedules import crontab
from django.conf import settings
import os

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_celery.settings')
app = Celery('django_celery')

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))


app.conf.beat_schedule = {
    "task_save_latest_flickr_image": {
        "task": "task_save_latest_flickr_image",
        "schedule": crontab(minute='*/15'),
    },
}