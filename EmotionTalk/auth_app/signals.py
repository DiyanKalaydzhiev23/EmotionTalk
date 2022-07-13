from django.db.models.signals import post_save
from django.dispatch import receiver
from EmotionTalk.auth_app.models import Profile
from EmotionTalk.auth_app.tasks import send_greeting_email


@receiver(post_save, sender=Profile)
def user_created(instance, created, *args, **kwargs):
    if created:
        return

    send_greeting_email.delay(instance.email)
