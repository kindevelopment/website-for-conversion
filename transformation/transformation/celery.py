import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'transformation.settings')

app = Celery('transformation')
app.config_from_object('django.conf.settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'every': {
        'task': 'transformapp.tasks.deleted_file_task',
        'schedule': crontab(minute=0, hour='*/2'),
    },

}

