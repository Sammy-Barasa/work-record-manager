# Generated by Django 3.1.2 on 2020-10-27 02:11

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('workrecords', '0003_auto_20201027_0207'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Workrecord',
            new_name='RecordOfWork',
        ),
    ]
