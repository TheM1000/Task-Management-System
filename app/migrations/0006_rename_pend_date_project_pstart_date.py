# Generated by Django 4.0.3 on 2022-05-18 14:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_payment_cheque_no_alter_payment_transaction_no'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='pend_date',
            new_name='pstart_date',
        ),
    ]
