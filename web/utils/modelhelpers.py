from django.db import models
from PIL import Image


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True, editable=False, verbose_name='Fecha de Creación')

    updated_at = models.DateTimeField(
        auto_now=True, editable=False, verbose_name='Útima Actualización')

    class Meta:
        abstract = True


def resize_image(*, image: models.ImageField, width: int, height: int) -> None:
    img = Image.open(image.path)

    image_resolution = (width, height)
    img.thumbnail(image_resolution, Image.ANTIALIAS)
    img.save(image.path)
