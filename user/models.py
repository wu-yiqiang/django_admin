from math import trunc

from django.db import models
from rest_framework import serializers

from common.db import BaseModel


# Create your models here.
class SysUser(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100, unique=True, verbose_name="用户名")
    password = models.CharField(max_length=100, verbose_name="密码")
    avatar = models.CharField(max_length=255, null=True, verbose_name="头像")
    email = models.CharField(max_length=100, null=True, verbose_name="Email")
    phonenumber = models.CharField(max_length=11, null=True, verbose_name="电话号码")
    login_date = models.DateField(null=True, verbose_name="登陆时间")
    status = models.IntegerField(null=True, verbose_name="状态值")
    create_time = models.DateField(null=True, verbose_name="创建时间")
    update_time = models.DateField(null=True, auto_now=True, verbose_name="更新时间")
    remark = models.CharField(max_length=1200, null=True, verbose_name="备注")

    class Meta:
        db_table = 'sys_user'
        verbose_name = "用户表"


class SysUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = SysUser
        fields = '__all__'
