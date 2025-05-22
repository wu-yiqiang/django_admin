from django.contrib import admin
from django.urls import path
from apps.buttons.views import CreateView, UpdateView, SearchPageView, SearchListsView, DetailView, DeleteView

app_name = 'button'
urlpatterns = [
    path('create', CreateView.as_view(), name='button_create'),
    path('page', SearchPageView.as_view(), name='button_page_list'),
    path('lists', SearchListsView.as_view(), name='button_list'),
    path('update', UpdateView.as_view(), name='button_update'),
    path('delete/<int:button_id>', DeleteView.as_view(), name='button_delete'),
    path("detail/<int:button_id>", DetailView.as_view(), name='button_detail'),
]
