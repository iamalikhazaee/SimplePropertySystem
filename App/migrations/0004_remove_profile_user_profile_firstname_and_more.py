# Generated by Django 4.1 on 2022-12-11 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0003_alter_contract_buyer_alter_contract_expert_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
        migrations.AddField(
            model_name='profile',
            name='firstname',
            field=models.CharField(default='ali', max_length=25),
        ),
        migrations.AddField(
            model_name='profile',
            name='lastname',
            field=models.CharField(default='kayzee', max_length=50),
        ),
        migrations.AddField(
            model_name='profile',
            name='password',
            field=models.CharField(default=' ', max_length=50),
        ),
        migrations.AddField(
            model_name='profile',
            name='username',
            field=models.CharField(default=' ', max_length=25),
        ),
    ]