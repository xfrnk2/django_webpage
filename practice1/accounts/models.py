from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models


# Create your models here.


class User(AbstractUser):

    # phone_number = models.CharField(max_length=13, blank=True, validators=[RegexValidator(r"%010-?[1-9]\d{3, 4}-?\d{4}$")])
    class Meta:
        verbose_name = '유저 정보'
        verbose_name_plural = '유저 정보 모음'
        ordering = ['id']