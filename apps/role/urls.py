from django.contrib import admin
from django.urls import path
from . import views

app_name = 'role'
urlpatterns = [
    path('create', views.RoleViewSet.as_view({"post": "create"}), name='role_create'),
    path('page', views.RoleViewSet.as_view({"post": "retrieve"}), name='role_pages'),
    path('lists', views.RoleViewSet.as_view({"get": "list"}), name='role_list'),
    path('update', views.RoleViewSet.as_view({"post": "update"}), name='role_update'),
    path('delete/<int:role_id>', views.RoleViewSet.as_view({"delete": "destroy"}), name='role_delete'),
    path('detail/<int:role_id>', views.RoleViewSet.as_view({"post": "details"}), name='role_detail'),
]
