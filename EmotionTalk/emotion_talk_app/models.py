from django.contrib.auth import get_user_model
from django.db import models


UserModel = get_user_model()


class Recording(models.Model):
    recording = models.FileField(
        upload_to='',
    )

    owner_id = models.IntegerField()
