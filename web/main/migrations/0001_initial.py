# Generated by Django 4.0.4 on 2022-05-01 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Baner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Útima Actualización')),
                ('title', models.CharField(max_length=50, verbose_name='Título')),
                ('subtitle', models.CharField(max_length=50, verbose_name='Subtítulo')),
                ('image', models.ImageField(help_text='Resolución Recomendada: 1920x688', upload_to='baner', verbose_name='Baner')),
                ('youtube_video', models.URLField(blank=True, help_text='Ejemplo: https://www.youtube.com/watch?v=7GWKv03Osek', null=True, verbose_name='Video Youtube')),
            ],
            options={
                'verbose_name': 'Baner',
                'verbose_name_plural': 'Baners',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Útima Actualización')),
                ('address', models.CharField(help_text='Ejemplo: A108 Adam Street New York, NY 535022 United States', max_length=100, verbose_name='Dirección')),
                ('email', models.EmailField(help_text='Ejemplo: correo@mail.com', max_length=254, verbose_name='Correo Electrónico')),
                ('phone_number', models.CharField(help_text='Ejemplo: +53 47281930', max_length=10, verbose_name='Número de teléfono')),
            ],
            options={
                'verbose_name': 'Información de Contacto',
                'verbose_name_plural': 'Informaciones de Contacto',
            },
        ),
        migrations.CreateModel(
            name='SocialLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Útima Actualización')),
                ('name', models.CharField(choices=[('FB', 'Facebook'), ('TW', 'Twitter'), ('IN', 'Instagram'), ('YT', 'Youtube'), ('LI', 'LinkedIn')], default='FB', max_length=2)),
                ('url', models.URLField(help_text='Ejemplo: https://www.twitter.com/', verbose_name='Dirección URL')),
            ],
            options={
                'verbose_name': 'Red Social',
                'verbose_name_plural': 'Redes Sociales',
            },
        ),
    ]
