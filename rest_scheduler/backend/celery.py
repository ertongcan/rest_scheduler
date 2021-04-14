from celery import Celery

import os


from django.conf import settings

app = Celery('backend')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

app.conf.update(BROKER_URL=os.environ['REDIS_URL'],
                CELERY_RESULT_BACKEND=os.environ['REDIS_URL'])
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rest_scheduler.settings')

@app.task
def test():
    print("Hello")