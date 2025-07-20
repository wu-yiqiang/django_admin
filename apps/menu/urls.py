from django.urls import path
from . import views

app_name = 'menu'
urlpatterns = [
    path('create', views.MenuViewSet.as_view({"post": "create"}), name='menu_create'),
    path('page', views.MenuViewSet.as_view({"post": "retrieve"}), name='menu_pages'),
    path('update', views.MenuViewSet.as_view({"post": "update"}), name='menu_update'),
    path('delete/<int:menu_id>', views.MenuViewSet.as_view({"delete": "destroy"}), name='menu_delete'),
    path('detail/<int:menu_id>', views.MenuViewSet.as_view({"get": "details"}), name='menu_detail'),
    path('permission/<int:menu_id>', views.MenuViewSet.as_view({"put": "permissions"}), name='menu_permission'),
    path('treeLists', views.MenuViewSet.as_view({"get": "trees"}), name='menu_tree'),
]
