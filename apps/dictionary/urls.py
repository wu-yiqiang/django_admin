from django.contrib import admin
from django.urls import path

from apps.dictionary.views import CreateView, SearchPageView, DeleteView, DetailView, UpdateView, SearchTypeListsView

app_name = 'dictionary'
urlpatterns = [
    path('create', CreateView.as_view(), name='dictionary_create'),
    path('page', SearchPageView.as_view(), name='dictionary_page'),
    path('types', SearchTypeListsView.as_view(), name='dictionary_type_list'),
    path('update', UpdateView.as_view(), name='dictionary_update'),
    path('delete/<int:dictionary_id>', DeleteView.as_view(), name='dictionary_delete'),
    path("detail/<int:dictionary_id>", DetailView.as_view(), name='dictionary_detail'),
]
