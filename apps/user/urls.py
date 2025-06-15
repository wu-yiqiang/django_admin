from django.contrib import admin
from django.urls import path
from apps.user.views import LoginView, LogoutView, UpdatePasswordView, RegisterView, \
    SearchPageView, SearchListsView, ExportView, UpdateAvatarView, UserViewSet

app_name = 'user'
urlpatterns = [
    path('login', LoginView.as_view(), name='user_login'),
    path('register', RegisterView.as_view(), name='user_register'),
    path('logout', LogoutView.as_view(), name='user_logout'),
    path('create', UserViewSet.as_view(), name='user_create'),
    path('update', UserViewSet.as_view(), name='user_update'),
    path('delete/<int:user_id>', UserViewSet.as_view(), name='user_delete'),
    path("detail/<int:user_id>", UserViewSet.as_view(), name='user_detail'),
    path('page', SearchPageView.as_view(), name='user_page_list'),
    path('lists', SearchListsView.as_view(), name='user_list'),
    path('update_avatar', UpdateAvatarView.as_view(), name='user_avatar_update'),
    path('update/password', UpdatePasswordView.as_view(), name='user_update'),
    path('download', ExportView.as_view(), name='user_export'),
    # path('lists', UserCreate.as_view(), name='user_lists'),
]
