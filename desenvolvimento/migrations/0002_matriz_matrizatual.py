# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('desenvolvimento', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='matriz',
            name='matrizAtual',
            field=models.ForeignKey(related_name='matrizatual', blank=True, to='desenvolvimento.Matriz', null=True),
        ),
    ]
