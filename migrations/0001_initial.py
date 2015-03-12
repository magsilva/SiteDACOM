__author__ = 'root'

from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


# class Migration(SchemaMigration):
# def forwards(self, orm):
#     # db.create_table(u'Professor',
#     #                 u'id, self.gf('django.db.models.fields.
#     # # def forwards(self, orm):
#     #     # Adding model 'CV'
    #     db.create_table(u'artigo',
    #         (u'id', self.gf('django.db.models.field.AutoField')(primary_key=True)),
    #         ('titulo', self.gf('django.db.models.field.CharField')(max_length=255)),
    #         ('data', self.gf('django.db.models.field.DateField')),
    #         ('doi', self.gf('django.db.models.field.CharField')(max_length=255)),
    #         ('paginaInicial', self.gf('django.db.models.field.CharField')(max_length=10)),
    #         ('paginaFinal', self.gf('django.db.models.field.CharField')(max_length=10)),
    #         ('Resumo', self.gf('django.db.models.field.CharField')(max_length=5000)()),
    #                     )
    #
    #     db.send_create_signal(u'artigo', ['Artigo'])
    #
    # def backwards(self, orm):
    #     # Deleting model 'CV'
    #     db.delete_table(u'artigo')
    #
    #
    # models = {
    #     u'desenvolvimento.artigo': {
    #         'Meta': {'object_name': 'Artigo'},
    #          u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
    #         #'lid': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
    #        # 'status': ('django.db.models.fields.SmallIntegerField', [], {})
    #         'titulo': ('django.db.models.field.CharField', [], {'max_length':'255'}),
    #         'data':('django.db.models.fields.DateField', [], {} ),
    #         'doi': ('django.db.models.fields.CharField',[], {'max_length':'255'}),
    #         'paginaInicial':('django.db.models.fields.CharField', [], {'max_length': '10'}),
    #         'paginaFinal': ('django.db.models.fields.CharField', [], {'max_length':'10'}),
    #         'Resumo':('django.db.models.fields.CharField', [], {'max_length': '5000'}),
    #
    #     }
    # }
    #
    # complete_apps = ['desenvolvimento']