from celery import shared_task
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.template.loader import render_to_string
from EmotionTalk import settings


UserModel = get_user_model()


@shared_task
def send_greeting_email(email):
    subject = "Registration greetings"
    html_message = "Hello dear user!"
    to = email
    send_mail(subject, '', settings.EMAIL_HOST_USER, [to], html_message=html_message)
