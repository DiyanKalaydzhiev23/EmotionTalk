from django.db.models.signals import pre_save
from django.dispatch import receiver
from EmotionTalk.auth_app.models import Profile
from EmotionTalk.auth_app.tasks import send_greeting_email


@receiver(pre_save, sender=Profile)
def send_email(instance, **kwargs):
    if instance in Profile.objects.all():
        return

    send_greeting_email.delay(instance.email)
