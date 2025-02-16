from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('user/', include('user.urls'),name='user'),
    path('role/', include('role.urls'), name='role'),
    path('menu/', include('menu.urls'),name='menu'),
]
