import base64
import datetime
import uuid
from io import BytesIO

from PIL import Image
import sys

from django.template.defaultfilters import slugify
from transliterate import slugify as trans_slugify

from .models import Image as img_model
from django.core.files import File


def transform(file_image, form_save):
    try:
        image = Image.open(BytesIO(base64.b64decode(file_image['img'])))
    except IOError:
        print("Unable to load image")
        sys.exit(1)
    png_io = BytesIO()
    image.save(png_io, 'png')
    name = uuid.uuid4()
    img = File(png_io, name=f'{name}.png')
    result = img_model.objects.get(pk=form_save)
    result.img = img
    slug = "_".join(str(result.img).split(".")[:-1])
    result.slug = slugify(slug)
    result.save()
