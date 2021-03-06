# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-02 05:09
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Parcel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(20)])),
                ('sender', models.CharField(blank=True, max_length=40, null=True)),
                ('date_delivered', models.DateField(auto_now_add=True)),
                ('date_received', models.DateField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Resident',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Email address')),
                ('enabled', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(700)])),
            ],
        ),
        migrations.AddField(
            model_name='resident',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.Room'),
        ),
        migrations.AddField(
            model_name='parcel',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.Room'),
        ),
    ]
