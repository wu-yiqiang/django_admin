from math import trunc
from django.db import models
from rest_framework import serializers
from common.db import BaseModel
from role.models import SysRole


# Create your models here.
class SysMenu(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=True, verbose_name="按钮名")
    icon = models.CharField(max_length=100, null=True, verbose_name="图标")
    parent_id = models.IntegerField(null=True, verbose_name="父级菜单")
    order_num = models.IntegerField(null=True, verbose_name="显示顺序")
    path = models.CharField(max_length=200, null=True, verbose_name="路由地址")
    component = models.CharField(max_length=200, null=True, verbose_name="组件路径")
    menu_type = models.CharField(max_length=1, null=True, verbose_name="菜单类型")
    perms = models.CharField(max_length=100, null=True, verbose_name="权限标识")
    create_time = models.DateField(null=True, verbose_name="创建时间")
    update_time = models.DateField(null=True, verbose_name="更新时间")
    remark = models.CharField(max_length=1200, null=True, verbose_name="备注")

    def __lt__(self, other):
        return self.order_name < other.order_name

    class Meta:
        db_table = 'sys_menu'
        verbose_name = "菜单表"


class SysRoleMenu(models.Model):
    id = models.AutoField(primary_key=True)
    role = models.ForeignKey(SysRole, on_delete=models.PROTECT)
    menu = models.ForeignKey(SysMenu, on_delete=models.PROTECT)

    class Meta:
        db_table = 'sys_role_menu'


class SysRoleMenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = SysRoleMenu
        fields = '__all__'
