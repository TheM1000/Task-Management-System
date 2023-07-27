# Generated by Django 4.0.3 on 2022-05-05 02:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_name', models.CharField(max_length=50, verbose_name='Empoyee Name')),
                ('emp_email', models.EmailField(max_length=254)),
                ('emp_password', models.CharField(max_length=10)),
                ('emp_phnumber', models.BigIntegerField()),
                ('emp_qualification', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('man_name', models.CharField(max_length=50, verbose_name='Manager Name')),
                ('man_email', models.EmailField(max_length=254)),
                ('man_password', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pay_name', models.CharField(default='', max_length=100, verbose_name='Payment To')),
                ('pay_amount', models.FloatField()),
                ('pay_date', models.DateField()),
                ('pay_status', models.BooleanField(default=False)),
                ('pay_type', models.CharField(max_length=100, verbose_name='Payment Through')),
                ('transaction_no', models.BigIntegerField()),
                ('cheque_no', models.BigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_name', models.CharField(default='', max_length=120, verbose_name='Task Name')),
                ('task_hour', models.FloatField(null=True)),
                ('task_cost', models.FloatField(null=True)),
                ('task_status', models.BooleanField(default=False)),
                ('task_priority', models.CharField(max_length=50, verbose_name='Task Priority')),
                ('employee', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=120, verbose_name='Project Name')),
                ('description', models.CharField(default=' ', max_length=500)),
                ('project_status', models.BooleanField(default=False)),
                ('project_date', models.DateTimeField(auto_now=True)),
                ('pbudget', models.FloatField(null=True)),
                ('pend_date', models.DateTimeField(blank=True, null=True)),
                ('ptotalcost', models.FloatField(null=True)),
                ('tasks', models.ManyToManyField(to='app.task')),
            ],
        ),
    ]
