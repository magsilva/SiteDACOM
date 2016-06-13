# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('desenvolvimento', '0016_auto_20160523_1459'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diadasemana',
            name='diaDaSemana',
            field=models.CharField(default=b'Segunda', max_length=10, choices=[(b'Segunda', b'Segunda'), (b'Terca', b'Terca'), (b'Quarta', b'Quarta'), (b'Quinta', b'Quinta'), (b'Sexta', b'Sexta'), (b'Sabado', b'Sabado')]),
        ),
    ]
