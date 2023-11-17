# ======导入模块======
from django.urls import path
from rest_framework.routers import DefaultRouter
from DrawingManagementSystem.views import SensorViewSet, ProjectViewSet, DataViewSet, DrawingViewSet

# ====1.实例化一个 DefaultRouter====
router = DefaultRouter()

# ====2.注册相应的url====
# 用户登录
# router.register('Login', LoginViewSet, basename='Login') # http://127.0.0.1:8080/DrawingApi/v1/Sensors/
# 注册Sensor对象
router.register('Sensors', SensorViewSet, basename='Sensors') # http://127.0.0.1:8080/DrawingApi/v1/Sensors/
# 注册Sensor对象
router.register('Projects', ProjectViewSet, basename='Projects') # http://127.0.0.1:8080/DrawingApi/v1/Projects/
# 注册Sensor对象
router.register('Datas', DataViewSet, basename='Datas') # http://127.0.0.1:8080/DrawingApi/v1/Datas/
# 注册Sensor对象
router.register('Drawings', DrawingViewSet, basename='Drawings') # http://127.0.0.1:8080/DrawingApi/v1/Drawings/

urlpatterns = []

# ====3.附加到urlpatterns集合中====
urlpatterns += router.urls
