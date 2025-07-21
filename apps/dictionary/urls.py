from django.contrib import admin
from django.urls import path
from . import views

app_name = 'dictionary'
urlpatterns = [
    path('create', views.DictionaryViewSet.as_view({"post": "create"}), name='dictionary_create'),
    path('page', views.DictionaryViewSet.as_view({"post": "retrieve"}), name='dictionary_pages'),
    path('types', views.DictionaryViewSet.as_view({"post": "types"}), name='dictionary_types'),
    path('update', views.DictionaryViewSet.as_view({"post": "update"}), name='dictionary_update'),
    path('delete/<int:dictionary_id>', views.DictionaryViewSet.as_view({"delete": "destroy"}),
         name='dictionary_delete'),
    path('detail/<int:dictionary_id>', views.DictionaryViewSet.as_view({"get": "details"}), name='dictionary_detail'),
]
