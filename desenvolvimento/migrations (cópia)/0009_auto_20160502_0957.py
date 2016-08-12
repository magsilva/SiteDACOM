# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('desenvolvimento', '0008_auto_20160502_0957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planodeaula',
            name='upload',
            field=models.FileField(null=True, upload_to=b'/home/humberto/Documentos/projectUtfpr/desenvolvimento/media//BCC/planoDeAula/2016/1', blank=True),
        ),
    ]
