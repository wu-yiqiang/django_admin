# Generated by Django 4.2.19 on 2025-07-05 14:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('net_disk', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='netdisk',
            old_name='fileName',
            new_name='file_name',
        ),
        migrations.RenameField(
            model_name='netdisk',
            old_name='fileSize',
            new_name='file_size',
        ),
        migrations.RenameField(
            model_name='netdisk',
            old_name='isFold',
            new_name='is_fold',
        ),
    ]
