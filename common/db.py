from django.db import models


class BaseModel(models.Model):
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间'),
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间'),
    is_delete = models.BooleanField(default=False, verbose_name='删除标记'),
    remark = models.CharField(max_length=1200, null=True, verbose_name="备注")

    class Meta:
        abstract = True
        verbose_name_plural = "公共字段表"
        db_table = "BaseTable"
