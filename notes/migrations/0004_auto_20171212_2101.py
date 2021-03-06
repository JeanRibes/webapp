# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-12 20:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0003_auto_20171212_2038'),
    ]

    operations = [
        migrations.CreateModel(
            name='MatiereModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_matiere', models.CharField(max_length=255, verbose_name='Matière')),
                ('coefficient', models.DecimalField(decimal_places=3, default=1, max_digits=4, verbose_name='Coefficient de la matière')),
            ],
            options={
                'verbose_name_plural': 'Matière',
            },
        ),
        migrations.AlterModelOptions(
            name='notesmodel',
            options={'verbose_name': 'note', 'verbose_name_plural': 'notes'},
        ),
        migrations.AlterField(
            model_name='notesmodel',
            name='coef',
            field=models.DecimalField(decimal_places=3, default=1, max_digits=4, verbose_name='coefficient'),
        ),
        migrations.AlterField(
            model_name='notesmodel',
            name='desc',
            field=models.CharField(blank=True, max_length=255, verbose_name='description du contrôle'),
        ),
        migrations.AlterField(
            model_name='notesmodel',
            name='matiere',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notes.MatiereModel', verbose_name='Matière'),
        ),
        migrations.AlterField(
            model_name='notesmodel',
            name='nom',
            field=models.CharField(max_length=255, verbose_name='nom du contrôle'),
        ),
    ]
