from django.contrib import admin
from django.urls import path
from . import views

app_name = 'user'
urlpatterns = [
    path('login', views.UserViewSet.as_view({"post": "login"}), name='user_login'),
    path('register', views.UserViewSet.as_view({"post": "register"}), name='user_register'),
    path('logout', views.UserViewSet.as_view({"post": "logout"}), name='user_logout'),
    path('create', views.UserViewSet.as_view({"post": "create"}), name='user_create'),
    path('update', views.UserViewSet.as_view({"put": "update"}), name='user_update'),
    path('delete/<int:user_id>', views.UserViewSet.as_view({"delete": "destroy"}), name='user_delete'),
    path("detail/<int:user_id>", views.UserViewSet.as_view({"get": "details"}), name='user_detail'),
    path('page', views.UserViewSet.as_view({"post": "retrieve"}), name='user_pages'),
    path('lists', views.UserViewSet.as_view({"post": "list"}), name='user_lists'),
    path('update_avatar', views.UserViewSet.as_view({"post": "update_avatar"}), name='user_avatar_update'),
    path('update/password', views.UserViewSet.as_view({"post": "update_password"}), name='user_update'),
    path('download', views.UserViewSet.as_view({"get": "export"}), name='user_export'),
]
