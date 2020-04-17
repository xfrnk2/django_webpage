"""django_tech URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import static
from django.contrib import admin
from django.urls import path, include
# from django_tech import settings
# from django.conf import global_settings
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog1/', include('blog1.urls')),
]

# 파일을 읽어서 응답을 주기 위한 방법
# 장고는 미디어 파일등의 스테틱 파일의 서빙을 실제 프로덕션에서 하는 것을 권장하지 않는다.
# 만약 if 문을 한 줄 없앤다 해도 빈 리스트를 반환하게 되지만, 명시적으로 사용하기 위해서 if문을 사용한다.
if settings.DEBUG:
    urlpatterns += static.static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)