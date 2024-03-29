# Generated by Django 4.0.3 on 2022-06-13 05:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0011_alter_task_description_alter_task_employee_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='description',
            field=models.TextField(default='', verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='task',
            name='employee',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='task',
            name='project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.project'),
        ),
        migrations.AlterField(
            model_name='task',
            name='task_cost',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='task_name',
            field=models.CharField(default='', max_length=120, verbose_name='Task Name'),
        ),
        migrations.AlterField(
            model_name='task',
            name='task_priority',
            field=models.CharField(max_length=50, verbose_name='Task Priority'),
        ),
    ]
