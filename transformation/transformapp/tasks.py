
from transformation.celery import app

from .service import transform, del_file


@app.task()
def deleted_file_task():
    del_file()

@app.task()
def get_image(file_image, form_save):
    transform(file_image, form_save)
