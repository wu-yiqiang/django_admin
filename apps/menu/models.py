from math import trunc
from django.db import models
from rest_framework import serializers

from apps.button.models import Button, ButtonSerializer
from apps.inteface.models import Inteface, IntefaceSerializer
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
    menu_type = models.IntegerField(null=False, verbose_name="菜单类型")
    code = models.CharField(max_length=100, null=True, verbose_name="权限标识")
    buttons = models.ManyToManyField(Button, related_name='menus')
    intefaces = models.ManyToManyField(Inteface, related_name='menus')

    def __lt__(self, other):
        return self.order_num < other.order_num

    class Meta:
        db_table = 'menu'
        verbose_name = "菜单表"


class MenuTreeSerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField()

    def get_children(self, obj):
        if hasattr(obj, "children"):
            serializerMenuList: list[MenuSerializer] = list()
            for sysMenu in obj.children:
                serializerMenuList.append(MenuSerializer(sysMenu).data)
            return serializerMenuList

    class Meta:
        model = Menu
        fields = '__all__'


class MenuSerializer(serializers.ModelSerializer):
    buttons = ButtonSerializer(many=True, read_only=True)
    intefaces = IntefaceSerializer(many=True, read_only=True)

    class Meta:
        model = Menu
        fields = '__all__'
