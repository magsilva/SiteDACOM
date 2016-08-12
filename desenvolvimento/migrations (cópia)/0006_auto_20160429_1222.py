# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('desenvolvimento', '0005_auto_20160425_1000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projeto',
            name='natureza',
            field=models.CharField(max_length=1000, null=True, verbose_name=b'Natureza', blank=True),
        ),
        migrations.AlterField(
            model_name='projeto',
            name='situacao',
            field=models.CharField(max_length=1000, null=True, verbose_name=b'Situacao', blank=True),
        ),
    ]
