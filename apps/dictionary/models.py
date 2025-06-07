from django.db import models
from rest_framework import serializers
from common.db import BaseModel


class Dictionary(BaseModel):
    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=255, null=False, verbose_name="字典类型")
    code = models.IntegerField(null=False, verbose_name="字典值")
    label = models.CharField(max_length=255, null=True, verbose_name="字典名")
    color = models.CharField(max_length=255, null=True, verbose_name="颜色值")
    bgColor = models.CharField(max_length=255, null=True, verbose_name="背景色")

    def __lt__(self, other):
        return self.order_num < other.order_num

    class Meta:
        db_table = 'dictionary'
        verbose_name = "字典表"


class DictionarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Dictionary
        field_order = ['id', 'type', 'code', 'label', 'is_deleted', 'remark', 'create_time', 'update_time']
        fields = '__all__'
