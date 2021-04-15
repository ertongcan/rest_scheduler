from celery import Celery

import os


from django.conf import settings

app = Celery('backend')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

app.conf.update(BROKER_URL=os.environ['REDIS_URL'], CELERY_RESULT_BACKEND='django-db',BEAT_SCHEDULER = 'django_celery_beat.schedulers:DatabaseScheduler')
app.config_from_object('django.conf:settings', namespace='CELERY')
@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))