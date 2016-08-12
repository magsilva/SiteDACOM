# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('desenvolvimento', '0017_auto_20160523_1504'),
    ]

    operations = [
        migrations.AddField(
            model_name='oferecimento',
            name='sala',
            field=models.CharField(default='', max_length=10, verbose_name=b'SalaDeAula'),
            preserve_default=False,
        ),
    ]
