# Generated by Django 4.1 on 2022-12-11 11:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0008_alter_contract_buyer_alter_contract_expert_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Price',
        ),
    ]
