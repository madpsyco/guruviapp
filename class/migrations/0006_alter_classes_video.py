# Generated by Django 4.1.7 on 2023-05-25 19:13

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('class', '0005_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classes',
            name='video',
            field=models.FileField(upload_to='videos_uploaded/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv'])]),
        ),
    ]
