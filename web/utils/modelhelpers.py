from django.db import models


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True, editable=False, verbose_name='Fecha de Creación')

    updated_at = models.DateTimeField(
        auto_now=True, editable=False, verbose_name='Útima Actualización')

    class Meta:
        abstract = True
