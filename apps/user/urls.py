from django.contrib import admin
from django.urls import path
from apps.user.views import LoginView, CreateView, LogoutView, UpdateView, UpdatePasswordView, RegisterView, \
    GetAssetsView, \
    SearchPageView, SearchListsView, DetailView, DeleteView, ExportView

app_name = 'user'
urlpatterns = [
    path('login', LoginView.as_view(), name='user_login'),
    path('register', RegisterView.as_view(), name='user_register'),
    path('logout', LogoutView.as_view(), name='user_logout'),
    path('create', CreateView.as_view(), name='user_create'),
    path('page', SearchPageView.as_view(), name='user_page_list'),
    path('lists', SearchListsView.as_view(), name='user_list'),
    path('update', UpdateView.as_view(), name='user_update'),
    path('delete/<int:user_id>', DeleteView.as_view(), name='user_delete'),
    path("detail/<int:user_id>", DetailView.as_view(), name='user_detail'),
    path('update/password', UpdatePasswordView.as_view(), name='user_update'),
    path('assets/page', GetAssetsView.as_view(), name='user_assets'),
    path('download', ExportView.as_view(), name='user_export'),
    # path('lists', UserCreate.as_view(), name='user_lists'),
]
