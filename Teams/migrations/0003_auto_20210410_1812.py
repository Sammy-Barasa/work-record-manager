# Generated by Django 3.1.7 on 2021-04-10 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Teams', '0002_auto_20210410_1740'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
