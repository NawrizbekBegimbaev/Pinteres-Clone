from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,include
from django.views.generic.base import TemplateView
from pinteres.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pinteres/',include('pinteres.urls'),name='pinteres'),
    path('register/success/',TemplateView.as_view(template_name='registration/success.html'),name='register-success'),
    path('register/',Register.as_view(),name='register'),
    path('login/',Login,name='login1'),
    path('accounts/',include('django.contrib.auth.urls'),name='account'),
    path('logout/',sign_out,name='logout')
]

urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)