from django.db import models
from rest_framework import serializers
from common.db import BaseModel


class Maintains(BaseModel):
    id = models.AutoField(primary_key=True)
    device_name = models.CharField(max_length=100, null=True, verbose_name="设备名")
    applyer = models.CharField(max_length=100, null=True, verbose_name="申请人")
    maintainer = models.CharField(max_length=100, null=True, verbose_name="维修人员")
    subject = models.CharField(max_length=100, null=True, verbose_name="主题")

    class Meta:
        db_table = 'maintains'
        verbose_name = "维修表"


class MaintainsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Maintains
        fields = '__all__'
        field_order = ['id', 'device_name', 'applyer', 'maintainer', 'subject', 'remark', 'create_time', 'update_time',
                       'is_deleted']
