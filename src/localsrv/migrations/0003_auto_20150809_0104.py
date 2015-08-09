# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('localsrv', '0002_auto_20150613_1213'),
    ]

    operations = [
        migrations.CreateModel(
            name='HttpResponse',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('path', models.CharField(max_length=255, blank=True)),
                ('headers', models.ManyToManyField(to='localsrv.ServableHttpHeader', blank=True)),
            ],
        ),
        migrations.RenameModel(
            old_name='FileSource',
            new_name='BodyFromFile',
        ),
        migrations.RenameModel(
            old_name='StringSource',
            new_name='BodyFromString',
        ),
        migrations.RenameModel(
            old_name='URLSource',
            new_name='BodyFromURL',
        ),
        migrations.RenameModel(
            old_name='Source',
            new_name='BodySource',
        ),
        migrations.RemoveField(
            model_name='servablecontent',
            name='headers',
        ),
        migrations.RemoveField(
            model_name='servablecontent',
            name='source',
        ),
        migrations.RenameField(
            model_name='bodyfromfile',
            old_name='source_ptr',
            new_name='bodysource_ptr',
        ),
        migrations.RenameField(
            model_name='bodyfromstring',
            old_name='source_ptr',
            new_name='bodysource_ptr',
        ),
        migrations.RenameField(
            model_name='bodyfromurl',
            old_name='source_ptr',
            new_name='bodysource_ptr',
        ),
        migrations.DeleteModel(
            name='ServableContent',
        ),
        migrations.AddField(
            model_name='httpresponse',
            name='source',
            field=models.ForeignKey(to='localsrv.BodySource', null=True),
        ),
    ]
