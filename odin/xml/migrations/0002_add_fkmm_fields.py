# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'ExampleModel.fk_field'
        db.add_column('xml_examplemodel', 'fk_field', self.gf('django.db.models.fields.related.ForeignKey')(default=1, related_name='fk_fields', to=orm['xml.RelatedModel']), keep_default=False)

        # Adding M2M table for field mm_field on 'ExampleModel'
        db.create_table('xml_examplemodel_mm_field', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('examplemodel', models.ForeignKey(orm['xml.examplemodel'], null=False)),
            ('relatedmodel', models.ForeignKey(orm['xml.relatedmodel'], null=False))
        ))
        db.create_unique('xml_examplemodel_mm_field', ['examplemodel_id', 'relatedmodel_id'])


    def backwards(self, orm):
        
        # Deleting field 'ExampleModel.fk_field'
        db.delete_column('xml_examplemodel', 'fk_field_id')

        # Removing M2M table for field mm_field on 'ExampleModel'
        db.delete_table('xml_examplemodel_mm_field')


    models = {
        'xml.examplemodel': {
            'Meta': {'object_name': 'ExampleModel'},
            'char_field': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'datetime_field': ('django.db.models.fields.DateTimeField', [], {}),
            'file_field': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'fk_field': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'fk_fields'", 'to': "orm['xml.RelatedModel']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'int_field': ('django.db.models.fields.IntegerField', [], {}),
            'mm_field': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'mm_fields'", 'symmetrical': 'False', 'to': "orm['xml.RelatedModel']"})
        },
        'xml.relatedmodel': {
            'Meta': {'object_name': 'RelatedModel'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '30', 'db_index': 'True'})
        }
    }

    complete_apps = ['xml']
