from math import trunc

from django.db import models
from rest_framework import serializers
from common.db import BaseModel
from user.models import SysUser


# Create your models here.
class SysRole(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, null=True, verbose_name="角色名")
    code = models.CharField(max_length=100, null=True, verbose_name="角色权限字符串")
    create_time = models.DateField(null=True, verbose_name="创建时间")
    update_time = models.DateField(null=True, verbose_name="更新时间")
    remark = models.CharField(max_length=1200, null=True, verbose_name="备注")

    class Meta:
        db_table = 'sys_role'
        verbose_name = "角色表"


class SysUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = SysRole
        fields = '__all__'


class SysUserRole(models.Model):
    id = models.AutoField(primary_key=True)
    role = models.ForeignKey(SysRole, on_delete=models.PROTECT)
    user = models.ForeignKey(SysUser, on_delete=models.PROTECT)

    class Meta:
        db_table = 'sys_user_role'


class SysUserRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = SysUserRole
        fields = '__all__'
