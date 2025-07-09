from django.db import models

# Create your models here.
from django.db import models
from rest_framework import serializers
from common.db import BaseModel


class NetDisk(BaseModel):
    id = models.AutoField(primary_key=True)
    url = models.CharField(max_length=255, null=False, verbose_name="访问地址")
    parent_id = models.IntegerField(null=True, verbose_name="父级地址")
    file_name = models.CharField(max_length=255, null=False, verbose_name="文件名")
    file_size = models.CharField(max_length=255, null=False, verbose_name="文件大小")
    is_fold = models.BooleanField(default=False, verbose_name="是否是文件夹")

    def __lt__(self, other):
        return self.order_num < other.order_num

    class Meta:
        db_table = 'net_disk'
        verbose_name = "文件表"


class NetDiskSerializer(serializers.ModelSerializer):
    class Meta:
        model = NetDisk
        fields = '__all__'
