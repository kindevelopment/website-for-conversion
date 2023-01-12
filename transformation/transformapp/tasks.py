from PIL import Image
import sys

def transform(file_image):
    try:
        image = Image.open(file_image)
    except IOError:
        print("Unable to load image")
        sys.exit(1)

    image.save(file_image, 'png')

