from math import trunc
from django.db import models
from rest_framework import serializers
from common.db import BaseModel


# from apps.role.models import Role


# Create your models here.
class Menu(BaseModel):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=True, verbose_name="按钮名")
    icon = models.CharField(max_length=100, null=True, verbose_name="图标")
    parent_id = models.IntegerField(null=True, verbose_name="父级菜单")
    order_num = models.IntegerField(null=True, verbose_name="显示顺序")
    path = models.CharField(max_length=300, null=True, verbose_name="路由地址")
    menu_type = models.CharField(max_length=1, null=True, verbose_name="菜单类型")
    code = models.CharField(max_length=100, null=True, verbose_name="权限标识")

    def __lt__(self, other):
        return self.order_num < other.order_num

    class Meta:
        db_table = 'menu'
        verbose_name = "菜单表"


class MenuSerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField()

    def get_children(self, obj):
        if hasattr(obj, "children"):
            serializerMenuList: list[MenuSerializer2] = list()
            for sysMenu in obj.children:
                serializerMenuList.append(MenuSerializer2(sysMenu).data)
            return serializerMenuList

    class Meta:
        model = Menu
        fields = '__all__'


class MenuSerializer2(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'

# class RoleMenu(models.Model):
#     id = models.AutoField(primary_key=True)
#     role = models.ForeignKey(Role, on_delete=models.PROTECT)
#     menu = models.ForeignKey(Menu, on_delete=models.PROTECT)
#
#     class Meta:
#         db_table = 'role_menu'
#
#
# class SysRoleMenuSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = RoleMenu
#         fields = '__all__'
