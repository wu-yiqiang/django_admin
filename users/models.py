from common.db import BaseModel
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser, BaseModel):
    mobile = models.CharField(verbose_name="手机号", default=12557080823, max_length=11)
    avatar = models.ImageField(verbose_name="用户头像", blank=True, null=True, validators="")
    class Meta:
        db_table = 'users'
        verbose_name = '用户表'

class VerifCode(models.Model):
    mobile = models.CharField(verbose_name="手机号", default=125570870823,max_length=11)
    code = models.CharField(verbose_name="验证码", default=880623,max_length=6)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    class Meta:
        db_table = 'verifcode'
        verbose_name = '验证码表'
