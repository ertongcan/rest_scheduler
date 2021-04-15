from celery import Celery

import os


from django.conf import settings

app = Celery('backend')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

app.conf.update(BROKER_URL=os.environ['REDIS_URL'], CELERY_RESULT_BACKEND=os.environ['REDIS_URL'],CELERYBEAT_SCHEDULER = 'djcelery.schedulers.DatabaseScheduler')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rest_scheduler.settings')

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))