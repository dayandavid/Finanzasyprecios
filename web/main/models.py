from utils.modelhelpers import TimeStampedModel
from django.db import models


class Contact(TimeStampedModel):

    address = models.CharField(
        "Dirección", max_length=100, help_text="Ejemplo: A108 Adam Street New York, NY 535022 United States")

    email = models.EmailField(
        verbose_name="Correo Electrónico", max_length=254, help_text="Ejemplo: correo@mail.com")

    phone_number = models.CharField(
        verbose_name="Número de teléfono", help_text="Ejemplo: +53 47281930", max_length=10)

    class Meta:
        verbose_name = "Contacto"
        verbose_name_plural = "Contactos"

    def __str__(self):
        return self.email


class SocialLink(TimeStampedModel):
    TWITTER = 'TW'
    FACEBOOK = 'FB'
    INSTAGRAM = 'IN'
    YOUTUBE = 'YT'
    LINKEDIN = 'LI'

    SOCIAL_NETWORKS = [
        (FACEBOOK, 'Facebook'),
        (TWITTER, 'Twitter'),
        (INSTAGRAM, 'Instagram'),
        (YOUTUBE, 'Youtube'),
        (LINKEDIN, 'LinkedIn'),
    ]
    name = models.CharField(
        max_length=2, choices=SOCIAL_NETWORKS, default=FACEBOOK)

    url = models.URLField(max_length=200, verbose_name="Dirección URL",
                          help_text="Ejemplo: https://www.twitter.com/")

    class Meta:
        verbose_name = "Red Social"
        verbose_name_plural = "Redes Sociales"

    def __str__(self):
        return self.name

    def get_full_name(self):
        return [item[1] for item in self.SOCIAL_NETWORKS if self.name == item[0]][0]
