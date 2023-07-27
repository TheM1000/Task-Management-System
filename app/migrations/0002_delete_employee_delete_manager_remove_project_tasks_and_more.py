# Generated by Django 4.0.3 on 2022-05-05 03:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Employee',
        ),
        migrations.DeleteModel(
            name='Manager',
        ),
        migrations.RemoveField(
            model_name='project',
            name='tasks',
        ),
        migrations.AddField(
            model_name='task',
            name='project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app.project'),
        ),
    ]