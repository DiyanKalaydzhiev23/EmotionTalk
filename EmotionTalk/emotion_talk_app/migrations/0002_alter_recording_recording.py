# Generated by Django 4.0.5 on 2022-07-17 10:19

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('emotion_talk_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recording',
            name='recording',
            field=cloudinary.models.CloudinaryField(max_length=255),
        ),
    ]
