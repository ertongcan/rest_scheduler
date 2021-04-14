import celery
app = celery.Celery('backend')
import os

from django.conf import settings
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

app.conf.update(BROKER_URL=os.environ['REDIS_URL'],
                CELERY_RESULT_BACKEND=os.environ['REDIS_URL'])
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')

@app.task
def add():
    return "Hello"