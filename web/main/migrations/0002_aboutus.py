# Generated by Django 4.0.4 on 2022-05-01 19:50

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Útima Actualización')),
                ('title', models.CharField(max_length=100, verbose_name='Título')),
                ('subtitle', models.CharField(blank=True, max_length=120, null=True, verbose_name='Subtítulo')),
                ('content', ckeditor.fields.RichTextField(verbose_name='Contenido')),
                ('image', models.ImageField(help_text='Resolución Recomendada: 992x950', upload_to='aboutus', verbose_name='Imagen')),
            ],
            options={
                'verbose_name': 'Nosotros',
                'verbose_name_plural': 'Nosotros',
            },
        ),
    ]