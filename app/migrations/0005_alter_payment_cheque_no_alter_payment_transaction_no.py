# Generated by Django 4.0.3 on 2022-05-05 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_rename_task_payment_task_remove_payment_pay_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='cheque_no',
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='payment',
            name='transaction_no',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]