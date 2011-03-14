# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'RelatedModel'
        db.create_table('xml_relatedmodel', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=30, db_index=True)),
        ))
        db.send_create_signal('xml', ['RelatedModel'])

        # Adding model 'ExampleModel'
        db.create_table('xml_examplemodel', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('char_field', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('datetime_field', self.gf('django.db.models.fields.DateTimeField')()),
            ('int_field', self.gf('django.db.models.fields.IntegerField')()),
            ('file_field', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
        ))
        db.send_create_signal('xml', ['ExampleModel'])


    def backwards(self, orm):
        
        # Deleting model 'RelatedModel'
        db.delete_table('xml_relatedmodel')

        # Deleting model 'ExampleModel'
        db.delete_table('xml_examplemodel')


    models = {
        'xml.examplemodel': {
            'Meta': {'object_name': 'ExampleModel'},
            'char_field': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'datetime_field': ('django.db.models.fields.DateTimeField', [], {}),
            'file_field': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'int_field': ('django.db.models.fields.IntegerField', [], {})
        },
        'xml.relatedmodel': {
            'Meta': {'object_name': 'RelatedModel'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '30', 'db_index': 'True'})
        }
    }

    complete_apps = ['xml']
