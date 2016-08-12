# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('desenvolvimento', '0023_artigo_datadeimportacao'),
    ]

    operations = [
        migrations.AddField(
            model_name='projeto',
            name='dataDeImportacao',
            field=models.CharField(max_length=15, null=True, verbose_name=b'Data', blank=True),
        ),
    ]
