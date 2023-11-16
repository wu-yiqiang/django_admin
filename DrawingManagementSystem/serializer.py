from rest_framework import serializers
from DrawingManagementSystem.models import Sensor, Project, Data, Drawing


# ----Sensor序列化类----
class SensorSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = "__all__"

# ____Project序列化类____
class ProjectSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"

# ____Data序列化类____
class DataSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Data
        fields = "__all__"

# ____Drawing序列化类____
class DrawingSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Drawing
        fields = "__all__"
