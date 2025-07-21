from django.urls import path
from . import views

app_name = 'button'
urlpatterns = [
    path('create', views.ButtonViewSet.as_view({"post": "create"}), name='button_create'),
    path('page', views.ButtonViewSet.as_view({"post": "retrieve"}), name='button_pages'),
    path('lists', views.ButtonViewSet.as_view({"get": "list"}), name='button_lists'),
    path('update', views.ButtonViewSet.as_view({"post": "update"}), name='button_update'),
    path('delete/<int:button_id>', views.ButtonViewSet.as_view({"delete": "destroy"}), name='button_delete'),
    path('detail/<int:button_id>', views.ButtonViewSet.as_view({"post": "details"}), name='button_detail'),
]
