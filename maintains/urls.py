from django.contrib import admin
from django.urls import path
from maintains.views import CreateView, UpdateView, SearchPageView, SearchListsView, DetailView, DeleteView

app_name = 'maintains'
urlpatterns = [
    # path('create', CreateView.as_view(), name='role_create'),
    path('page', SearchPageView.as_view(), name='role_page_list'),
]
