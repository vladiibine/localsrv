# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('localsrv', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filesource',
            name='file_path',
            field=models.FilePathField(null=True),
        ),
    ]
