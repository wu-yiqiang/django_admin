from django.db import models
from rest_framework import serializers
from django.contrib.auth.models import AbstractUser, AbstractBaseUser

from apps.button.models import ButtonSerializer
from apps.inteface.models import IntefaceSerializer
from apps.menu.models import MenuSerializer, Menu
from common.db import BaseModel
from apps.role.models import Role, RoleSerializer


class User(BaseModel):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100, unique=True, verbose_name="用户名")
    password = models.CharField(max_length=100, verbose_name="密码")
    avatar = models.CharField(max_length=255, null=True, verbose_name="头像")
    email = models.CharField(max_length=100, null=True, verbose_name="Email")
    phone_number = models.CharField(max_length=11, null=True, verbose_name="电话号码")
    login_date = models.DateField(null=True, verbose_name="登陆时间")
    status = models.IntegerField(null=True, verbose_name="状态值")
    roles = models.ManyToManyField(Role, related_name='users')

    # class Meta:
    #     db_table = 'user'
    #     verbose_name = "用户表"
    #
    # def get_role_permission(self):
    #     return RoleSerializer(self.roles.values(), many=True).data
    #
    # def get_role_permission_id(self):
    #     return list(self.roles.values_list('id', flat=True))
    #
    # def get_menu_permission(self):
    #     roleIds = self.get_role_permission_id()
    #     menuLists = []
    #     for roleId in roleIds:
    #         roleItem = RoleSerializer(Role.objects.filter(id=roleId).values(), many=True).data
    #         print('sssss', roleItem)
    #         # for menu in menus:
    #         #     menuItem = Role.objects.filter(id=menu.id)
    #         #     menuLists.append(menuItem)
    #     # return menus.distinct()
    #
    # def get_button_permission(self):
    #     buttons = [x for x in self.roles.values_list('buttons', flat=True) if x]
    #     return list(ButtonSerializer(buttons, many=True).data)
    #
    # def get_inteface_permission(self):
    #     intefaces = [x for x in self.roles.values_list('intefaces', flat=True) if x]
    #     return list(IntefaceSerializer(intefaces, many=True).data)
    #
    # def get_user_permissions(self):
    #     return {
    #         'id': self.id,
    #         'username': self.username,
    #         'email': self.email,
    #         'phone_number': self.phone_number,
    #         'avatar': self.avatar,
    #         'status': self.status,
    #         'login_date': self.login_date,
    #         'roles': self.get_role_permission(),
    #         'menus': self.get_menu_permission(),
    #         # 'buttons': self.get_button_permission(),
    #         # 'inteface': self.get_inteface_permission(),
    #     }


class UserSerializer(serializers.ModelSerializer):
    roles = RoleSerializer(many=True, read_only=True)

    class Meta:
        model = User
        field_order = [
            'id', 'username', 'password', 'avatar', 'roles', 'email', 'phone_number', 'login_date',
            'status',
            'is_deleted',
            'remark',
            'create_time', 'update_time']
        # fields = '__all__'
        exclude = ['password']
