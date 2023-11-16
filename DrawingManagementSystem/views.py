# ====== 导入模块 ======
from rest_framework.viewsets import ModelViewSet   # 封装完成的ModelViewset视图集
from DrawingManagementSystem.models import Sensor, Project, Data, Drawing   # 具体的类
from DrawingManagementSystem.serializer import SensorSerialzer, ProjectSerialzer, DataSerialzer, DrawingSerialzer # 序列化类

# ---Sensor视图---
class SensorViewSet(ModelViewSet):
      queryset = Sensor.objects.all()
      serializer_class = SensorSerialzer

# ---Project---
class ProjectViewSet(ModelViewSet):
      queryset = Project.objects.all()
      serializer_class = ProjectSerialzer

# ---Data视图---
class DataViewSet(ModelViewSet):
      queryset = Data.objects.all()
      serializer_class = DataSerialzer

# ---Sensor视图---
class DrawingViewSet(ModelViewSet):
      queryset = Drawing.objects.all()
      serializer_class = DrawingSerialzer
