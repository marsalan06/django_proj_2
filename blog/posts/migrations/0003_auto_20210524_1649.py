# Generated by Django 3.1.7 on 2021-05-24 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20210524_0846'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='thumbnail',
            field=models.ImageField(null=True, upload_to='upload/'),
        ),
    ]
