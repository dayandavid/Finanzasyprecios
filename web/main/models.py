from tabnanny import verbose
from utils.modelhelpers import TimeStampedModel, resize_image
from django.db import models
from ckeditor.fields import RichTextField


class Contact(TimeStampedModel):

    address = models.CharField(
        "Dirección", max_length=100, help_text="Ejemplo: A108 Adam Street New York, NY 535022 United States")

    email = models.EmailField(
        verbose_name="Correo Electrónico", max_length=254, help_text="Ejemplo: correo@mail.com")

    phone_number = models.CharField(
        verbose_name="Número de teléfono", help_text="Ejemplo: +53 47281930", max_length=10)

    class Meta:
        verbose_name = "Información de Contacto"
        verbose_name_plural = "Informaciones de Contacto"

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


class Baner(TimeStampedModel):
    title = models.CharField(verbose_name="Título", max_length=50)
    subtitle = models.CharField(verbose_name="Subtítulo", max_length=50)
    image = models.ImageField(verbose_name="Baner", upload_to='baner',
                              height_field=None, width_field=None, max_length=None, help_text='Resolución Recomendada: 1920x688')
    youtube_video = models.URLField(
        verbose_name='Video Youtube', max_length=200, help_text='Ejemplo: https://www.youtube.com/watch?v=7GWKv03Osek', null=True, blank=True)

    class Meta:
        verbose_name = "Baner"
        verbose_name_plural = "Baners"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super().save(args, kwargs)

        resize_image(image=self.image, width=1700, height=609)


class AboutUs(TimeStampedModel):
    title = models.CharField(verbose_name='Título', max_length=100)

    subtitle = models.CharField(
        verbose_name='Subtítulo', max_length=120, null=True, blank=True)

    content = RichTextField(verbose_name='Contenido')

    mision = models.TextField(verbose_name='Misión', null=True, blank=True)

    vision = models.TextField(verbose_name='Visión', null=True, blank=True)

    image = models.ImageField(verbose_name='Imagen', upload_to='aboutus', height_field=None,
                              width_field=None, max_length=None, help_text='Resolución Recomendada: 992x950')

    class Meta:
        verbose_name = "Nosotros"
        verbose_name_plural = "Nosotros"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super().save(args, kwargs)

        resize_image(image=self.image, width=992, height=950)


class Service(TimeStampedModel):
    name = models.CharField(verbose_name="Nombre", max_length=50)

    slug = models.SlugField(verbose_name="Nombre URL",
                            help_text="Este campo es generado automáticamente")

    short_description = models.CharField(
        verbose_name="Pequeña Descripción", max_length=100)

    long_description = RichTextField(verbose_name="Descripción")

    show = models.BooleanField(
        verbose_name="Mostrar", default=False, help_text="Chequear para mostrar en la página")

    class Meta:
        verbose_name = "Servicio"
        verbose_name_plural = "Servicios"

    def __str__(self):
        return self.name
