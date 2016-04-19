# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('desenvolvimento', '0002_matriz_matrizatual'),
    ]

    operations = [
        migrations.AddField(
            model_name='curso',
            name='matrizAtual',
            field=models.ForeignKey(related_name='matrizNome', blank=True, to='desenvolvimento.Matriz', null=True),
        ),
    ]
