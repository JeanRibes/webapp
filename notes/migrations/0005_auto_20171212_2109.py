# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-12 20:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0004_auto_20171212_2101'),
    ]

    operations = [
        migrations.CreateModel(
            name='TypeNote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typeNote', models.CharField(max_length=20, verbose_name='Type de note')),
            ],
            options={
                'verbose_name': 'type',
                'verbose_name_plural': 'type de note',
            },
        ),
        migrations.AlterModelOptions(
            name='matieremodel',
            options={'verbose_name': 'Matière', 'verbose_name_plural': 'Matière'},
        ),
    ]