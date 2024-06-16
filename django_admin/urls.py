from django.contrib import admin
from django.urls import path, include

from django.contrib import admin
from django.urls import path, include

# 使用 drf_yasg API文档生成器 视图和openapi
from django.views.static import serve
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# 导入权限控制模块
from rest_framework import permissions

# 文档视图
schema_view = get_schema_view(
    # API 信息
    openapi.Info(
        title='接口文档',   # API文档标题
        default_version='V1',   # 版本信息
        description='接口文档',    # 描述内容
        # terms_of_service='https://qaq.com',    # 开发团队地址
        # contact=openapi.Contact(email='https://qaq.@qq.com',url='https://qaq.com'),   # 联系人信息：邮件、网址
        # license=openapi.License(name='qaq License'),    # 证书
    ),
    public=True,    # 是否公开
    # permission_classes=(permissions.AllowAny,)   # 设置用户权限

)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),  # 互动模式
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),  # 文档模式
    path('api/users/', include('users.urls')),
]
