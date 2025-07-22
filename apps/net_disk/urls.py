from django.contrib import admin
from django.urls import path
from . import views

app_name = 'net_disk'
urlpatterns = [
    path('upload', views.NetDiskViewSet.as_view({"post": "upload"}), name='net_disk_upload'),
    path('current_files', views.NetDiskViewSet.as_view({"post": "current_files"}), name='net_disk_current_files'),
    path('tree_list', views.NetDiskViewSet.as_view({"get": "tree_list"}), name='net_disk_tree_list'),
    path('batch_update', views.NetDiskViewSet.as_view({"post": "batch_update"}), name='net_disk_batch_update'),
    path('create_fold', views.NetDiskViewSet.as_view({"post": "create_fold"}), name='create_fold'),
    path('delete', views.NetDiskViewSet.as_view({"post": "delete"}), name='delete'),

]
