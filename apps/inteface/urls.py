from django.urls import path
from apps.inteface.views import CreateView, SearchPageView, UpdateView, DeleteView, DetailView, SearchListsView

app_name = 'inteface'
urlpatterns = [
    path('create', CreateView.as_view(), name='inteface_create'),
    path('page', SearchPageView.as_view(), name='inteface_page_lists'),
    path('lists', SearchListsView.as_view(), name='inteface_lists'),
    path('update', UpdateView.as_view(), name='inteface_update'),
    path('delete/<int:inteface_id>', DeleteView.as_view(), name='inteface_delete'),
    path('detail/<int:inteface_id>', DetailView.as_view(), name='inteface_detail'),
]
