from django.contrib import admin
from django.urls import path
from . import views
app_name = 'testers'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name = 'index'),
    path('questions/', views.regConTester, name='regCon'),
    path('questions2/', views.showQuestions, name='allQuestions'),
    path('conQuestion/', views.conQuestions, name='conQuestion'),
]
