# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-22 18:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0009_auto_20170309_1841'),
    ]

    operations = [
        migrations.CreateModel(
            name='AssociadoFamilia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'família',
                'verbose_name_plural': 'famílias',
            },
        ),
        migrations.RemoveField(
            model_name='associado',
            name='familia',
        ),
        migrations.AddField(
            model_name='associadofamilia',
            name='associado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadastro.Associado', verbose_name='associado'),
        ),
        migrations.AddField(
            model_name='associadofamilia',
            name='familia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadastro.Familia', verbose_name='familia'),
        ),
    ]