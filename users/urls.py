from django.urls import path, include
from users.views import LoginView

urlpatterns = [
    path('login/', LoginView.as_view()),
]
