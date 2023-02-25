# Generated by Django 3.2 on 2022-11-23 11:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sell_price', models.CharField(max_length=12)),
                ('rent_price', models.CharField(max_length=12)),
                ('deposit', models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meterage', models.CharField(max_length=10)),
                ('construction_year', models.CharField(max_length=10)),
                ('neighborhood_name', models.CharField(max_length=50)),
                ('parking', models.BooleanField()),
                ('type', models.CharField(choices=[('sale', 'sale'), ('rent', 'rent')], max_length=12)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.profile')),
                ('price', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.price')),
            ],
        ),
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('first agreement', 'first agreement'), ('second agreement', 'second agreement')], max_length=20)),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='buyer', to='App.profile')),
                ('expert', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='expert', to='App.profile')),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.property')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seller', to='App.profile')),
            ],
        ),
    ]
