# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('desenvolvimento', '0007_auto_20160502_0913'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planodeaula',
            name='upload',
            field=models.FileField(null=True, upload_to=b'/home/humberto/Documentos/projectUtfpr/desenvolvimento/static//BCC/planoDeAula/2016/1', blank=True),
        ),
    ]
