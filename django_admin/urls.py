from django.conf import settings
from django.urls import path, include, re_path
from django.views.static import serve
from django_admin.views import UploadView
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path('schema', SpectacularAPIView.as_view(), name='schema'),
    path('swagger', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('user/', include('user.urls'), name='user'),
    path('role/', include('role.urls'), name='role'),
    path('menu/', include('menu.urls'), name='menu'),
    path('button/', include('button.urls'), name='button'),
    path('dictionary/', include('dictionary.urls'), name='dictionary'),
    path('inteface/', include('inteface.urls'), name='inteface'),
    path('net_disk/', include('net_disk.urls'), name='inteface'),

    path('upload', UploadView.as_view(), name='upload'),
    # path('upload/netdisk', UploadNetView.as_view(), name='upload_netdisk'),
    # path('netdisk/get', GetUploadView.as_view(), name='get_netdisk'),
    re_path('storage/(?P<path>.*)', serve, {"document_root": settings.MEDIA_ROOT}, name="storage"),

]
