# Generated by Django 3.1.7 on 2021-04-05 08:42

from django.db import migrations
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('workrecords', '0012_auto_20210324_0954'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personchoises',
            name='phone',
            field=phone_field.models.PhoneField(blank=True, help_text='Contact phone number', max_length=31),
        ),
    ]
