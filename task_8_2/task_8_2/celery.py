from __future__ import absolute_import
import os
from celery import Celery
from django.conf import settings

# встановлюємо стандартні Django налаштування для celery.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'task_8_2.settings')
app = Celery('task_8_2a')

# Використвуємо строку для того, щоб воркер не приховав об'єкт при використанні Windows
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)



@app.task(bind=True)
def print_hello():
    print('hello there')