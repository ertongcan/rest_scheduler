from celery import Celery

import os


from django.conf import settings




#app.conf.update(broker_url=os.environ['REDIS_URL'], result_backend='db+postgresql://ekoexsuklgioqd:25b88e9cbc9e790817071769167d7e5bf8154acb57f3972b3b0d9f484709e61c@ec2-34-233-0-64.compute-1.amazonaws.com:5432/d8m0j5mj2fdmpi', BEAT_SCHEDULER = 'django_celery_beat.schedulers.DatabaseScheduler')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rest_scheduler.settings')

app = Celery('backend')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))