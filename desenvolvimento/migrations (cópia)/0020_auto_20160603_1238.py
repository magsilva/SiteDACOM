# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('desenvolvimento', '0019_infraestrutura_sala'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='centroacademico',
            name='informacao',
        ),
        migrations.RemoveField(
            model_name='empresajunior',
            name='informacao',
        ),
        migrations.AddField(
            model_name='centroacademico',
            name='linkParaAPage',
            field=models.CharField(max_length=100, null=True, verbose_name=b'linkParaAPage', blank=True),
        ),
        migrations.AddField(
            model_name='centroacademico',
            name='linkParaoSite',
            field=models.CharField(max_length=100, null=True, verbose_name=b'linkParaoSite', blank=True),
        ),
        migrations.AddField(
            model_name='empresajunior',
            name='linkParaAPage',
            field=models.CharField(max_length=100, null=True, verbose_name=b'linkParaAPage', blank=True),
        ),
        migrations.AddField(
            model_name='empresajunior',
            name='linkParaoSite',
            field=models.CharField(max_length=100, null=True, verbose_name=b'linkParaoSite', blank=True),
        ),
    ]
