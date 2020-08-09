from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
class User(AbstractUser):
    website_url = models.URLField(blank=True)
    bio = models.TextField(blank=True)

    def send_welcome_email(self):
        subject = render_to_string("accounts/welcome_email_subject.txt", {'user':self})
        content = render_to_string("accounts/welcome_email_content.txt", {'user':self})
        sender_email = settings.WELCOME_EMAIL_SENDER

        send_mail(subject, content, sender_email, [self.email], fail_silently=False)
