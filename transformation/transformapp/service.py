import base64
import io
from io import BytesIO

from PIL import Image
import sys

from transformation.settings import MEDIA_ROOT
from .models import Image as img_model
from django.core.files import File


def transform(file_image, form_save):
    try:
        image = Image.open(file_image)
    except IOError:
        print("Unable to load image")
        sys.exit(1)
    png_io = BytesIO()
    image.save(png_io, 'png')
    name = ''.join(file_image.name.split('.')[:-1])
    img = File(png_io, name=f'{name}.png')
    result = img_model.objects.get(pk=form_save.id)
    result.img = img
    result.save()