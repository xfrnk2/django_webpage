from django.conf import settings
from django.db import models

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=6)#, validators=[] 숫자의 형태로만 zipcode가 입력이 되도록 유효성검사 로직에 제한을 걸을 수 있게 된다.