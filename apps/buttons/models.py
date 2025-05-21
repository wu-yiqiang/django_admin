from django.db import models
from rest_framework import serializers
from common.db import BaseModel


class Button(BaseModel):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=True, verbose_name="按钮名")
    code = models.CharField(max_length=100, null=True, verbose_name="标识")

    def __lt__(self, other):
        return self.order_num < other.order_num

    class Meta:
        db_table = 'button'
        verbose_name = "按钮表"


class SysButtonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Button
        field_order = ['id', 'username', 'code', 'is_deleted', 'remark', 'create_time', 'update_time']
