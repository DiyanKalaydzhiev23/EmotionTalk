# Generated by Django 4.0.5 on 2022-07-17 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emotion_talk_app', '0002_alter_recording_recording'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recording',
            name='recording',
            field=models.FileField(upload_to=''),
        ),
    ]
