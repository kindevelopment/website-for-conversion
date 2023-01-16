from transformation.celery import app

from .service import transform


@app.task
def get_image(file_image, form_save):
    transform(file_image, form_save)