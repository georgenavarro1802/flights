# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-04 18:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Airline',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Airlines',
                'verbose_name': 'Airline',
                'db_table': 'airlines',
            },
        ),
        migrations.CreateModel(
            name='Airplane',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
                ('passengers', models.IntegerField(default=0)),
                ('fuel_capacity', models.FloatField(default=0)),
                ('fuel_consumption', models.FloatField(default=0)),
            ],
            options={
                'verbose_name_plural': 'Airplanes',
                'verbose_name': 'Airplane',
                'db_table': 'airplanes',
            },
        ),
        migrations.CreateModel(
            name='Airport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('lat', models.FloatField(blank=True, null=True)),
                ('lng', models.FloatField(blank=True, null=True)),
                ('active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'Airports',
                'verbose_name': 'Airport',
                'db_table': 'airports',
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Cities',
                'verbose_name': 'City',
                'db_table': 'cities',
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('symbol', models.CharField(max_length=2)),
            ],
            options={
                'verbose_name_plural': 'Countries',
                'verbose_name': 'Country',
                'db_table': 'countries',
            },
        ),
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.IntegerField(choices=[(1, 'MONDAY'), (2, 'TUESDAY'), (3, 'WEDNESDAY'), (4, 'THURSDAY'), (5, 'FRIDAY'), (6, 'SATURDAY'), (7, 'SUNDAY')], default=1)),
                ('departure', models.TimeField()),
                ('arrival', models.TimeField()),
                ('airline', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='air.Airline')),
                ('airplane', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='air.Airplane')),
                ('destination', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='destination', to='air.Airport')),
                ('origin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='origin', to='air.Airport')),
            ],
            options={
                'verbose_name_plural': 'Flights',
                'verbose_name': 'Flight',
                'db_table': 'flights',
            },
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='air.Country')),
            ],
            options={
                'verbose_name_plural': 'States',
                'verbose_name': 'State',
                'db_table': 'states',
            },
        ),
        migrations.AlterUniqueTogether(
            name='country',
            unique_together=set([('name',)]),
        ),
        migrations.AddField(
            model_name='city',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='air.State'),
        ),
        migrations.AddField(
            model_name='airport',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='air.City'),
        ),
        migrations.AlterUniqueTogether(
            name='airplane',
            unique_together=set([('brand', 'model')]),
        ),
        migrations.AddField(
            model_name='airline',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='air.Country'),
        ),
        migrations.AlterUniqueTogether(
            name='state',
            unique_together=set([('name', 'country')]),
        ),
        migrations.AlterUniqueTogether(
            name='city',
            unique_together=set([('name', 'state')]),
        ),
        migrations.AlterUniqueTogether(
            name='airport',
            unique_together=set([('name', 'city')]),
        ),
        migrations.AlterUniqueTogether(
            name='airline',
            unique_together=set([('name', 'country')]),
        ),
    ]
