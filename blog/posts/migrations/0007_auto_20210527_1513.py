# Generated by Django 3.1.7 on 2021-05-27 10:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_gallery'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='gallery',
            options={'verbose_name': 'Gallery', 'verbose_name_plural': 'Galleries'},
        ),
        migrations.AlterModelTable(
            name='gallery',
            table='Gallery',
        ),
    ]