# Generated by Django 4.2.19 on 2025-02-16 15:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_alter_sysuser_table'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sysuser',
            old_name='loggin_date',
            new_name='login_date',
        ),
    ]
