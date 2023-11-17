
from django.contrib import admin
from django.urls import path
from django.urls import path,include
from drf_yasg.views import  get_schema_view
from drf_yasg import openapi
schema_view = get_schema_view(
    openapi.Info(
        title='api接口文档',
        default_version='v1',
        description="接口文档",
        terms_of_service="",
        contact=openapi.Contact(email="wu_yiqiang@outlook.com"),
        license=openapi.License(name="MIT License")
    ),
    public=True,
    # permission_classes=(permission.AllowAny,),
)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('DrawingApi/v1/', include('DrawingManagementSystem.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0),name="schema-swagger-ui"),
]
