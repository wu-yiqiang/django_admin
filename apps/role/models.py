from math import trunc
from django.db import models
from rest_framework import serializers
from common.db import BaseModel
from apps.menu.models import Menu, MenuSerializer
from apps.inteface.models import Inteface, IntefaceSerializer
from apps.button.models import Button, ButtonSerializer


# from apps.user.models import User


class Role(BaseModel):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, null=True, verbose_name="角色名")
    code = models.CharField(max_length=100, null=True, verbose_name="角色权限字符串")
    menus = models.ManyToManyField(Menu, related_name='roles')
    buttons = models.ManyToManyField(Button, related_name='roles')
    intefaces = models.ManyToManyField(Inteface, related_name='roles')

    class Meta:
        db_table = 'role'
        verbose_name = "角色表"


class RoleSerializer(serializers.ModelSerializer):
    menus = MenuSerializer(many=True, read_only=True)
    buttons = ButtonSerializer(many=True, read_only=True)
    intefaces = IntefaceSerializer(many=True, read_only=True)

    class Meta:
        model = Role
        fields = '__all__'
        field_order = ['id', 'name', 'code', 'menus', 'buttons', 'intefaces', 'is_deleted', 'remark', 'create_time',
                       'update_time']
