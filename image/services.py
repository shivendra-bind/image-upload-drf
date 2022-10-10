from typing import TextIO, BinaryIO
from .models import Image
def create_image(*, image:TextIO | BinaryIO):
    img = Image(image)
    image.save()
    return image