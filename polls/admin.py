# 점 경로는 현재 경로를 의미한다
# Register your models here.
from django.contrib import admin
from .models import Question

admin.site.register(Question)