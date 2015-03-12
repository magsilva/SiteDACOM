# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'CV.categoria'
        db.add_column(u'proxy_cv', 'categoria',
                      self.gf('django.db.models.fields.CharField')(default=0, max_length=2),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'CV.categoria'
        db.delete_column(u'proxy_cv', 'categoria')


    models = {
        u'proxy.cv': {
            'Meta': {'object_name': 'CV'},
            'categoria': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lid': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'status': ('django.db.models.fields.SmallIntegerField', [], {})
        }
    }

    complete_apps = ['proxy']