from django.db import models

# === 图纸管理系统 models
# 传感器分类--sensor， 项目--project， 资料-data， 图纸信息-drawing

# 公有创建时间和修改时间
class TimestampMode(models.Model):
    """
    An abstract base class model that provides selfupdating ``created`` and ``modified`` fields.
    """
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True  # it's very important to add this line


# === 传感器类 --- Sensor：Id,name,created,modified
class Sensor(TimestampMode):
    sensor_name = models.CharField(verbose_name="传感器名称", max_length=50, unique=True, null=False, blank=False)

    # create_time = models.DateTimeField(default=timezone.now().replace(microsecond=0))

    class Meta:
        db_table = "Draw_Sensor"
        managed = True
        app_label = "DrawingManagementSystem"

    def __str__(self):
        return "%s" % (self.sensor_name)


# === 项目类 --- project：Id,name,created,modified
class Project(TimestampMode):
    project_name = models.CharField(verbose_name="项目名称", max_length=50, unique=True, null=False, blank=False)
    sensor = models.ForeignKey(verbose_name="所属传感器", to=Sensor, on_delete=models.PROTECT)

    class Meta:
        db_table = "Draw_Project"
        managed = True
        app_label = "DrawingManagementSystem"

    def __str__(self):
        return "%s" % (self.project_name)

# === 资料类 --- data:ID,name,created,modified
class Data(TimestampMode):
    data_name = models.CharField(verbose_name="资料名称", max_length=50, unique=True, null=False, blank=False)
    sensor = models.ForeignKey(verbose_name="所属传感器", to=Sensor, on_delete=models.PROTECT)
    project = models.ForeignKey(verbose_name="所属项目", to=Project, on_delete=models.PROTECT)

    class Meta:
        db_table = "Draw_Data"
        managed = True
        app_label = "DrawingManagementSystem"

    def __str__(self):
        return "%s" % (self.data_name)
# === 图纸信息 --- drawing:ID(Material_code),drawing_name,created,modified,drawing_spec,drawing_page,drawing_client_id,drawing_remark,drawing_version
class Drawing(TimestampMode):
    material_code = models.CharField(verbose_name="物料编号", max_length=50, blank=False)
    sensor = models.ForeignKey(verbose_name="所属传感器", to=Sensor, on_delete=models.PROTECT)
    project = models.ForeignKey(verbose_name="所属项目", to=Project, on_delete=models.PROTECT)
    data = models.ForeignKey(verbose_name="所属资料", to=Data, on_delete=models.PROTECT)
    drawing_name = models.CharField(verbose_name="材料名称", max_length=50, blank=False)
    drawing_spec = models.CharField(verbose_name="规格/图纸号", max_length=50, blank=False)
    drawing_page = models.CharField(verbose_name="图纸页数", max_length=50, blank=False)
    drawing_client_id = models.CharField(verbose_name="客户编号", max_length=50)
    drawing_version = models.CharField(verbose_name="版本号", max_length=50, blank=False)
    drawing_remark = models.CharField(verbose_name="备注", max_length=100)
    drawing_url = models.CharField(verbose_name="地址", max_length=100)
    is_deleted = models.IntegerField(verbose_name="逻辑删除0否1是", blank=False, default=0)

    class Meta:
        db_table = "Draw_Drawing"
        managed = True
        app_label = "DrawingManagementSystem"

    def __str__(self):
        return "%s" % (self.drawing_name)

