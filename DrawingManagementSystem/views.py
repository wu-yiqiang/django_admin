# ====== 导入模块 ======
from rest_framework.viewsets import ModelViewSet    # 封装完成的ModelViewset视图集
from DrawingManagementSystem.models import Sensor, Project, Data, Drawing    # 具体的类
from DrawingManagementSystem.serializer import SensorSerialzer, ProjectSerialzer, DataSerialzer, \
        DrawingSerialzer    # 序列化类
from django_filters.rest_framework import DjangoFilterBackend    # 实现筛选的后台模块
from DrawingManagementSystem.filter import SensorFilter, ProjectFilter, DataFilter, DrawingFilter
from DrawingManagementSystem.paginations import MyPageNumberPagination
# ---Sensor视图---
class SensorViewSet(ModelViewSet):
        queryset = Sensor.objects.all()
        serializer_class = SensorSerialzer
        # 指定筛选的类
        filter_class = SensorFilter

# ---Project---
class ProjectViewSet(ModelViewSet):
        queryset = Project.objects.all()
        serializer_class = ProjectSerialzer
        # 指定筛选的类
        filter_class = ProjectFilter
 
# ---Data视图---
class DataViewSet(ModelViewSet):
        queryset = Data.objects.all()
        serializer_class = DataSerialzer
        # 指定筛选的类
        filter_class = DataFilter

# ---Sensor视图---
class DrawingViewSet(ModelViewSet):
        queryset = Drawing.objects.all()
        serializer_class = DrawingSerialzer
        pagination_class = MyPageNumberPagination
        # 指定筛选的类
        filter_class = DrawingFilter
        # 指定查找匹配的字段
        search_fields = ('drawing_name', 'material_code', 'drawing_spec', 'drawing_client_id')
