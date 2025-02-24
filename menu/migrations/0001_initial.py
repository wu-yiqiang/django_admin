# Generated by Django 4.2.19 on 2025-02-22 09:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SysMenu',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, null=True, verbose_name='按钮名')),
                ('icon', models.CharField(max_length=100, null=True, verbose_name='图标')),
                ('parent_id', models.IntegerField(null=True, verbose_name='父级菜单')),
                ('order_name', models.IntegerField(null=True, verbose_name='显示顺序')),
                ('path', models.CharField(max_length=200, null=True, verbose_name='路由地址')),
                ('component', models.CharField(max_length=200, null=True, verbose_name='组件路径')),
                ('menu_type', models.CharField(max_length=1, null=True, verbose_name='菜单类型')),
                ('perms', models.CharField(max_length=100, null=True, verbose_name='权限标识')),
                ('create_time', models.DateField(null=True, verbose_name='创建时间')),
                ('update_time', models.DateField(null=True, verbose_name='更新时间')),
                ('remark', models.CharField(max_length=1200, null=True, verbose_name='备注')),
            ],
            options={
                'verbose_name': '菜单表',
                'db_table': 'sys_menu',
            },
        ),
        migrations.CreateModel(
            name='SysRoleMenu',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='menu.sysmenu')),
            ],
            options={
                'db_table': 'sys_role_menu',
            },
        ),
    ]
