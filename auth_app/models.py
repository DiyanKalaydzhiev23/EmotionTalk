from django.db import models
from django.contrib.auth import models as auth_models
from EmotionTalk.auth_app.managers import EmotionTalkUserManager
from django.contrib.postgres.fields import ArrayField


class EmotionTalkUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    username = models.CharField(
        max_length=25,
        unique=True,
    )

    date_joined = models.DateTimeField(
        auto_now_add=True,
    )

    is_staff = models.BooleanField(
        default=False,
    )

    USERNAME_FIELD = 'username'

    objects = EmotionTalkUserManager()


class Profile(models.Model):
    email = models.EmailField(
        unique=True,
    )

    image = models.ImageField(
        upload_to='images',
        default='images/default_image_qvmqoi.png',
    )

    receive_data_users = ArrayField(
        models.IntegerField(),
        default=list,
    )

    pending_users_to_send_data_to = ArrayField(
        models.IntegerField(),
        default=list,
    )

    user = models.OneToOneField(
        EmotionTalkUser,
        on_delete=models.CASCADE,
        primary_key=True,
    )


class ResetPasswordData(models.Model):
    user_id = models.IntegerField()

    token = models.CharField(
        max_length=150
    )

    token_submit = models.BooleanField(
        default=False,
    )
