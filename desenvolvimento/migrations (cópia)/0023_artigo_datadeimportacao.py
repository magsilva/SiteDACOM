# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('desenvolvimento', '0022_auto_20160812_1528'),
    ]

    operations = [
        migrations.AddField(
            model_name='artigo',
            name='dataDeImportacao',
            field=models.CharField(max_length=15, null=True, verbose_name=b'DataDeImportacaoDosDados', blank=True),
        ),
    ]
