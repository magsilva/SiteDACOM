# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('desenvolvimento', '0006_auto_20160429_1222'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='matriz',
            name='matrizAtual',
        ),
        migrations.AddField(
            model_name='curso',
            name='regulamentacao',
            field=models.CharField(max_length=1000, null=True, verbose_name=b'Regulamentacao', blank=True),
        ),
        migrations.AddField(
            model_name='relacaodisciplinacurso',
            name='matriz',
            field=models.ForeignKey(related_name='matrizAtual', blank=True, to='desenvolvimento.Matriz', null=True),
        ),
    ]
