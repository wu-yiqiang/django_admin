from django.db import models
from rest_framework import serializers
from common.db import BaseModel


# Create your models here.
class Inteface(BaseModel):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=True, verbose_name="接口名")
    type = models.IntegerField(null=True, verbose_name="接口类型")
    path = models.CharField(max_length=200, null=True, verbose_name="接口路径")

    # def __lt__(self, other):
    #     return self.order_num < other.order_num

    class Meta:
        db_table = 'inteface'
        verbose_name = "接口表"


class IntefaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inteface
        fields = '__all__'
