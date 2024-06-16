from common.db import BaseModel
from django.contrib.auth.models import AbstractUser, AbstractBaseUser
from django.db import models


class User(AbstractUser, BaseModel):
    email = models.EmailField(verbose_name="邮箱", default="wu_yiqiang@outlook.com", max_length=11, unique=True)
    login_type = models.BooleanField(default=0, verbose_name="用户类型", max_length=1)
    avatar = models.ImageField(verbose_name="用户头像", blank=True, null=True, validators="")
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['login_type', 'password']
    class Meta:
        db_table = 'users'
        verbose_name = '用户表'

