# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'CV'
        db.create_table(u'proxy_cv', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('lid', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('status', self.gf('django.db.models.fields.SmallIntegerField')()),
        ))
        db.send_create_signal(u'proxy', ['CV'])


    def backwards(self, orm):
        # Deleting model 'CV'
        db.delete_table(u'proxy_cv')


    models = {
        u'proxy.cv': {
            'Meta': {'object_name': 'CV'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lid': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'status': ('django.db.models.fields.SmallIntegerField', [], {})
        }
    }

    complete_apps = ['proxy']