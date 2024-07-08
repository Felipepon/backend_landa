from myproject.celery import shared_task
from .script import descargar_documento_dane

@shared_task
def tarea_descargar_documento_dane():
    descargar_documento_dane()
