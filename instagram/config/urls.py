from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django.contrib.auth.decorators import login_required
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django_pydenticon.views import image as pydenticon_image 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('identicon/image/<path:data>/', pydenticon_image, name='pydenticon_image',),
    path('', login_required(TemplateView.as_view(template_name='root.html')), name='root'), # 아무 주소를 넣어도 최상위 주소로 매칭이 된다.
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]


    urlpatterns += static(settings.MEDIA_URL,
            document_root=settings.MEDIA_ROOT)
