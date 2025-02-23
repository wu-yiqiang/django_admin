from django.contrib import admin
from django.urls import path
from user.views import LoginView, CreateView, LogoutView, UpdateView, UpdatePasswordView, RegisterView

app_name = 'user'
urlpatterns = [
    path('login', LoginView.as_view(), name='user_login'),
    path('register', RegisterView.as_view(), name='user_register'),
    path('logout', LogoutView.as_view(), name='user_logout'),
    path('create', CreateView.as_view(), name='user_create'),
    path('update/password', UpdatePasswordView.as_view(), name='user_update'),
    path('update', UpdateView.as_view(), name='user_update'),
    # path('lists', UserCreate.as_view(), name='user_lists'),
]
