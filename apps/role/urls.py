from django.contrib import admin
from django.urls import path
from .views import CreateView, UpdateView, SearchPageView, SearchListsView, DetailView, DeleteView

app_name = 'role'
urlpatterns = [
    path('create', CreateView.as_view(), name='role_create'),
    path('page', SearchPageView.as_view(), name='role_page_list'),
    path('lists', SearchListsView.as_view(), name='role_list'),
    path('update', UpdateView.as_view(), name='role_update'),
    path('delete/<int:role_id>', DeleteView.as_view(), name='role_delete'),
    path("detail/<int:role_id>", DetailView.as_view(), name='role_detail'),
]
