from django.db import models


class BaseModel(models.Model):
    is_deleted = models.BooleanField(null=False, default=False, verbose_name='删除标记')
    remark = models.CharField(max_length=2500, null=True, verbose_name="备注")
    update_time = models.DateField(null=True, auto_now=True, verbose_name="更新时间")
    create_time = models.DateField(null=True, verbose_name="创建时间")

    class Meta:
        abstract = True
        verbose_name_plural = "公共字段表"
        db_table = "BaseTable"
