# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('desenvolvimento', '0012_auto_20160502_1507'),
    ]

    operations = [
        migrations.AddField(
            model_name='matriz',
            name='numero',
            field=models.IntegerField(default=0),
        ),
    ]
