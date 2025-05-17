from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve
from django_admin.settings import base
from django_admin.views import UploadView

urlpatterns = [
    path('user/', include('user.urls'), name='user'),
    path('role/', include('role.urls'), name='role'),
    path('menu/', include('menu.urls'), name='menu'),
    path('maintain/', include('maintains.urls'), name='menu'),
    path('upload', UploadView.as_view(), name='upload'),
    re_path('media/(?P<path>.*)', serve, {"document_root": base.MEDIA_ROOT}, name="media"),
]
