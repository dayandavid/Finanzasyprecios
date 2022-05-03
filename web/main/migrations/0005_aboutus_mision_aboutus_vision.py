# Generated by Django 4.0.4 on 2022-05-02 21:12

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_service_show'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutus',
            name='mision',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Misión'),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='vision',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Visión'),
        ),
    ]
