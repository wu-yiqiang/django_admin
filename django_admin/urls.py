from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve
from django_admin import settings

urlpatterns = [
    path('user/', include('user.urls'), name='user'),
    path('role/', include('role.urls'), name='role'),
    path('menu/', include('menu.urls'), name='menu'),
    re_path('media/(?P<path>.*)', serve, {"document_root": settings.MEDIA_ROOT}, name="media"),
]
