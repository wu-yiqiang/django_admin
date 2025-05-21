from math import trunc
from django.db import models
from rest_framework import serializers
from common.db import BaseModel
from apps.role.models import SysRole


# Create your models here.
class SysMenu(BaseModel):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=True, verbose_name="按钮名")
    icon = models.CharField(max_length=100, null=True, verbose_name="图标")
    parent_id = models.IntegerField(null=True, verbose_name="父级菜单")
    order_num = models.IntegerField(null=True, verbose_name="显示顺序")
    path = models.CharField(max_length=200, null=True, verbose_name="路由地址")
    menu_type = models.CharField(max_length=1, null=True, verbose_name="菜单类型")
    code = models.CharField(max_length=100, null=True, verbose_name="权限标识")

    def __lt__(self, other):
        return self.order_num < other.order_num

    class Meta:
        db_table = 'sys_menu'
        verbose_name = "菜单表"


class SysMenuSerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField()

    def get_children(self, obj):
        print("111")
        if hasattr(obj, "children"):
            serializerMenuList: list[SysMenuSerializer2] = list()
            for sysMenu in obj.children:
                serializerMenuList.append(SysMenuSerializer2(sysMenu).data)
            return serializerMenuList

    class Meta:
        model = SysMenu
        fields = '__all__'


class SysMenuSerializer2(serializers.ModelSerializer):
    class Meta:
        model = SysMenu
        fields = '__all__'


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
