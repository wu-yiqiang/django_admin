from django.contrib import admin
from django.urls import path
from user.views import LoginView, UserView

app_name ='user'
urlpatterns = [
   path('login', LoginView.as_view(), name='user_login'),
   path('lists', UserView.as_view(), name='user_lists'),
]
