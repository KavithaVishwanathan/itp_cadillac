# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-14 23:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EB', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cardetailsupdate',
            fields=[
                ('carid', models.CharField(blank=True, db_column='CarId', max_length=10, null=True)),
                ('updateid', models.CharField(db_column='UpdateId', max_length=10, primary_key=True, serialize=False)),
                ('caryear', models.IntegerField(blank=True, db_column='CarYear', null=True)),
                ('carnum', models.IntegerField(blank=True, db_column='CarNum', null=True)),
                ('title', models.CharField(blank=True, db_column='Title', max_length=30, null=True)),
                ('content', models.TextField(blank=True, db_column='Content', null=True)),
                ('createdby', models.CharField(blank=True, db_column='CreatedBy', max_length=50, null=True)),
                ('createdate', models.DateTimeField(blank=True, db_column='CreateDate', null=True)),
                ('lastupdatedate', models.DateTimeField(blank=True, db_column='LastUpdateDate', null=True)),
                ('jalbumlink', models.CharField(blank=True, db_column='JAlbumLink', max_length=100, null=True)),
            ],
            options={
                'db_table': 'CarDetailsUpdate',
            },
        ),
    ]
