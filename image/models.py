from django.db import models
from uuid import uuid4
from pathlib import Path


def upload_to(instance, filename):
    name = uuid4()
    path = Path(filename)
    file_name = f"{name}{path.suffix}"
    if instance.name is None:
        instance.name = f"{path.stem}{path.suffix}"
    return f"images/{file_name}"


class Image(models.Model):
    image = models.ImageField(upload_to=upload_to)
    alt_text = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    