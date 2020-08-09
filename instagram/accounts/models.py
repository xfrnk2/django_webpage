from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    website_url = models.URLField(blank=True)
<<<<<<< HEAD
    bio = models.TextField(blank=True)

    def send_welcome_email(self):
        pass
=======
    bio = models.TextField(blank=True)
>>>>>>> parent of d9a8c09... add function in models.py\User : send_welcome_email
