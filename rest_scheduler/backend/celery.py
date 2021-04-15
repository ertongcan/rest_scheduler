from celery import Celery

import os


from django.conf import settings

app = Celery('backend')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

app.conf.update(broker_url=os.environ['REDIS_URL'], result_backend=os.environ['REDIS_URL'], BEAT_SCHEDULER = 'django_celery_beat.schedulers.DatabaseScheduler')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rest_scheduler.settings')

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))