# Generated by Django 4.1 on 2022-12-11 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0011_contract_tracking_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='tracking_code',
            field=models.PositiveIntegerField(default=0),
        ),
    ]