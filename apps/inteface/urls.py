from django.urls import path
from . import views

app_name = 'inteface'
urlpatterns = [
    path('create', views.IntefaceViewSet.as_view({"post": "create"}), name='inteface_create'),
    path('page', views.IntefaceViewSet.as_view({"post": "retrieve"}), name='inteface_pages'),
    path('lists', views.IntefaceViewSet.as_view({"post": "list"}), name='inteface_list'),
    path('update', views.IntefaceViewSet.as_view({"post": "update"}), name='inteface_update'),
    path('delete/<int:inteface_id>', views.IntefaceViewSet.as_view({"delete": "destroy"}), name='inteface_delete'),
    path('detail/<int:inteface_id>', views.IntefaceViewSet.as_view({"get": "details"}), name='inteface_detail'),
]
