from django.urls import path
from apps.menu.views import CreateView, TreeListView, SearchPageView, UpdateView, DeleteView, DetailView, \
    SetMenuPermission

app_name = 'menu'
urlpatterns = [
    path('create', CreateView.as_view(), name='menu_create'),
    path('page', SearchPageView.as_view(), name='menu_page_lists'),
    path('update', UpdateView.as_view(), name='menu_update'),
    path('delete/<int:menu_id>', DeleteView.as_view(), name='menu_delete'),
    path('detail/<int:menu_id>', DetailView.as_view(), name='menu_detail'),
    path('permission/<int:menu_id>', SetMenuPermission.as_view(), name='menu_permission'),
    path('treeLists', TreeListView.as_view(), name='tree_lists'),

]
