from math import trunc

from django.db import models
from rest_framework import serializers
from common.db import BaseModel
from apps.user.models import User


# from  apps.user.apps import User

class SysRole(BaseModel):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, null=True, verbose_name="角色名")
    code = models.CharField(max_length=100, null=True, verbose_name="角色权限字符串")

    class Meta:
        db_table = 'role'
        verbose_name = "角色表"


class SysRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = SysRole
        fields = '__all__'
        field_order = ['id', 'name', 'code', 'is_deleted', 'remark', 'create_time', 'update_time']


class SysUserRole(models.Model):
    id = models.AutoField(primary_key=True)
    role = models.ForeignKey(SysRole, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.PROTECT)

    class Meta:
        db_table = 'sys_user_role'


class SysUserRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = SysUserRole
        fields = '__all__'
