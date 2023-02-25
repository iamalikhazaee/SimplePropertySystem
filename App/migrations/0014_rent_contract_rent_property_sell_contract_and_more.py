# Generated by Django 4.1 on 2023-01-24 07:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0013_customer_alter_contract_tracking_code'),
    ]

    operations = [
        migrations.CreateModel(
            name='rent_Contract',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('first agreement', 'first agreement'), ('second agreement', 'second agreement')], max_length=20)),
                ('tracking_code', models.CharField(default=' ', max_length=20)),
                ('expert', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rent_expert', to='App.profile')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owner', to='App.profile')),
            ],
        ),
        migrations.CreateModel(
            name='rent_Property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meterage', models.CharField(max_length=10)),
                ('construction_year', models.CharField(max_length=10)),
                ('neighborhood_name', models.CharField(max_length=50)),
                ('parking', models.BooleanField()),
                ('rent_price', models.PositiveIntegerField(default=0)),
                ('deposit', models.PositiveIntegerField(default=0)),
                ('approve', models.BooleanField(default=False)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.profile')),
            ],
        ),
        migrations.CreateModel(
            name='sell_Contract',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('first agreement', 'first agreement'), ('second agreement', 'second agreement')], max_length=20)),
                ('tracking_code', models.CharField(default=' ', max_length=20)),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='buyer', to='App.profile')),
                ('expert', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sell_expert', to='App.profile')),
            ],
        ),
        migrations.CreateModel(
            name='sell_Property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meterage', models.CharField(max_length=10)),
                ('construction_year', models.CharField(max_length=10)),
                ('neighborhood_name', models.CharField(max_length=50)),
                ('parking', models.BooleanField()),
                ('sell_price', models.PositiveIntegerField(default=0)),
                ('approve', models.BooleanField(default=False)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.profile')),
            ],
        ),
        migrations.RemoveField(
            model_name='property',
            name='owner',
        ),
        migrations.DeleteModel(
            name='Contract',
        ),
        migrations.DeleteModel(
            name='Property',
        ),
        migrations.AddField(
            model_name='sell_contract',
            name='property',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.sell_property'),
        ),
        migrations.AddField(
            model_name='sell_contract',
            name='seller',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seller', to='App.profile'),
        ),
        migrations.AddField(
            model_name='rent_contract',
            name='property',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.rent_property'),
        ),
        migrations.AddField(
            model_name='rent_contract',
            name='renter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='renter', to='App.profile'),
        ),
    ]
