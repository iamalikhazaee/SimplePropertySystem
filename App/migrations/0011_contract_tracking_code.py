# Generated by Django 4.1 on 2022-12-11 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0010_property_approve'),
    ]

    operations = [
        migrations.AddField(
            model_name='contract',
            name='tracking_code',
            field=models.CharField(default=' ', max_length=15),
        ),
    ]
