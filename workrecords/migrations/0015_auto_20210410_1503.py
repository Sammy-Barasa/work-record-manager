# Generated by Django 3.1.7 on 2021-04-10 15:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('workrecords', '0014_work_date_paid'),
    ]

    operations = [
        migrations.AddField(
            model_name='work',
            name='assigned_to',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='given_to', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='work',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='owner', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='work',
            name='assigned_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='workrecords.personchoises'),
        ),
    ]