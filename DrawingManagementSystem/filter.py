from django_filters import FilterSet
from DrawingManagementSystem.models import Sensor, Project, Data, Drawing
from django_filters import FilterSet,filters


# ---Sensor的Filter类---
class SensorFilter(FilterSet):
        # 重新需要支持模糊匹配的字段
        sensor_name = filters.CharFilter(field_name='sensor_name', lookup_expr="icontains")
        class Meta:
                model = Sensor
                fields = ('sensor_name',) # 传感器名称


# ---Project的Filter类---
class ProjectFilter(FilterSet):
        project_name = filters.CharFilter(field_name='project_name', lookup_expr="icontains")
        class Meta:
                model = Project
                fields = ('project_name', 'sensor') # 项目名称 所属传感器


# ---Data的Filter类---
class DataFilter(FilterSet):
        data_name = filters.CharFilter(field_name='data_name', lookup_expr="icontains")
        class Meta:
                model = Data
                fields = ('data_name', 'sensor', 'project') # 资料名称 所属传感器 所属项目


# ---Drawing的Filter类---
class DrawingFilter(FilterSet):
        # 重新需要支持模糊匹配的字段
        drawing_name = filters.CharFilter(field_name='drawing_name', lookup_expr="icontains")
        material_code = filters.CharFilter(field_name='material_code', lookup_expr="icontains")
        drawing_spec = filters.CharFilter(field_name='drawing_spec', lookup_expr="icontains")
        drawing_client_id = filters.CharFilter(field_name='drawing_client_id', lookup_expr="icontains")
        class Meta:
                model = Drawing
                fields = ('drawing_name', 'material_code', 'drawing_spec', 'drawing_client_id') # 材料名称、物料编号、规格/图纸号、客户编号
