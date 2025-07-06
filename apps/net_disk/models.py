from django.db import models

# Create your models here.
from django.db import models
from rest_framework import serializers
from common.db import BaseModel


class NetDisk(BaseModel):
    id = models.AutoField(primary_key=True)
    url = models.CharField(max_length=255, null=False, verbose_name="访问地址")
    parentId = models.IntegerField(null=True, verbose_name="父级地址")
    fileName = models.CharField(max_length=255, null=False, verbose_name="文件名")
    fileSize = models.CharField(max_length=255, null=False, verbose_name="文件大小")
    isFold = models.BooleanField(default=False, verbose_name="是否是文件夹")

    def __lt__(self, other):
        return self.order_num < other.order_num

    class Meta:
        db_table = 'net_disk'
        verbose_name = "文件表"


class NetDiskSerializer(serializers.ModelSerializer):
    class Meta:
        model = NetDisk
        field_order = ['id', 'url', 'fileName', 'fileSize', 'isFold', 'is_deleted', 'remark', 'create_time',
                       'update_time']
        fields = '__all__'
