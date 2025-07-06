from django.contrib import admin
from django.urls import path
from apps.net_disk.views import UploadNetView, GetUploadView, CreateFoldView

app_name = 'net_disk'
urlpatterns = [
    # path('create', CreateView.as_view(), name='button_create'),
    # path('page', SearchPageView.as_view(), name='button_page_list'),
    # path('lists', SearchListsView.as_view(), name='button_list'),
    # path('update', UpdateView.as_view(), name='button_update'),
    # path('delete/<int:button_id>', DeleteView.as_view(), name='button_delete'),
    # path("detail/<int:button_id>", DetailView.as_view(), name='button_detail'),
    path('upload', UploadNetView.as_view(), name='upload'),
    path('create_fold', CreateFoldView.as_view(), name='create_fold'),
    path('current_files', GetUploadView.as_view(), name='current_lists'),
]
