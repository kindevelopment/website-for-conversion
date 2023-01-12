import base64
import io
from io import BytesIO

from PIL import Image
import sys

from django.core.files import File


def transform(file_image):
    try:
        image = Image.open(io.BytesIO(base64.b64decode(file_image)))
    except IOError:
        print("Unable to load image")
        sys.exit(1)
    png_io = BytesIO()
    image.save(png_io, 'png')
    name = ''.join(file_image.name.split('.')[:-1])
    img = File(png_io, name=f'{name}.png')
    return img
