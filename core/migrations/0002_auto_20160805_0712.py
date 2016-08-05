# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-05 02:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='angrys',
            field=models.IntegerField(db_index=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='author_id',
            field=models.TextField(db_index=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='comments',
            field=models.IntegerField(db_index=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='hahas',
            field=models.IntegerField(db_index=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='likes',
            field=models.IntegerField(db_index=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='loves',
            field=models.IntegerField(db_index=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='published',
            field=models.DateTimeField(db_index=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='reactions',
            field=models.IntegerField(db_index=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='sads',
            field=models.IntegerField(db_index=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='shares',
            field=models.IntegerField(db_index=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='wows',
            field=models.IntegerField(db_index=True),
        ),
    ]
