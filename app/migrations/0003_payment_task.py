# Generated by Django 4.0.3 on 2022-05-05 03:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_delete_employee_delete_manager_remove_project_tasks_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='task',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='app.task'),
            preserve_default=False,
        ),
    ]
