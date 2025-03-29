from math import trunc

from django.db import models
from rest_framework import serializers
from django.contrib.auth.models import AbstractUser, AbstractBaseUser
from common.db import BaseModel


# Create your models here.
class User(BaseModel):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100, unique=True, verbose_name="用户名")
    password = models.CharField(max_length=100, verbose_name="密码")
    avatar = models.CharField(max_length=255, null=True, verbose_name="头像")
    email = models.CharField(max_length=100, null=True, verbose_name="Email")
    phone_number = models.CharField(max_length=11, null=True, verbose_name="电话号码")
    login_date = models.DateField(null=True, verbose_name="登陆时间")
    status = models.IntegerField(null=True, verbose_name="状态值")

    class Meta:
        db_table = 'user'
        verbose_name = "用户表"


class SysUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        field_order = [
            'id', 'username', 'password', 'avatar', 'email', 'phone_number', 'login_date', 'status', 'is_deleted',
            'remark',
            'create_time', 'update_time']
        # fields = '__all__'
        exclude = ['password']
