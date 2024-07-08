from __future__ import absolute_import, unicode_literals
import os
from myproject.celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tu_proyecto.settings')

app = Celery('MYPROJECT')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

from celery.schedules import crontab

app.conf.beat_schedule = {
    'descargar-documento-cada-dia': {
        'task': 'mi_app.tasks.tarea_descargar_documento_dane',
        'schedule': crontab(hour=0, minute=0),  # Esto ejecuta la tarea todos los días a medianoche
    },
}
