#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from xml.etree import cElementTree as ElementTree

class XmlExporter(object):

    def __init__(self, queryset):
        self.queryset = queryset
        if self.queryset:
            self.meta = self.queryset[0]._meta
        else:
            self.meta = None

    def contribute_to_class(self, instance):
        pass


    def set_filename(self):
        if self.meta
            filename = '%s_%s.xml' %(self.meta.app_label, self.meta.module_name.lower())
        else:
            filename = 'odin_xml.xml'
        return filename


    def save(self, save_dir, filename=''):
        if not filename:
            self.set_filename()

        if not os.path.exists(save_dir):
            os.makedirs(save_dir)
        file_path = os.path.join(save_dir, filename)
        
        # nodes
        if self.meta:
            root = ElementTree.Element('root_%s' % sef.meta.module_name.lower())
        else:
            root = ElementTree.Element('root_odin')

        for instance in self.queryset:        
            self.contribute_to_class(instance)
            for field in instance._meta.fields:
                field_type = field.get_internal_type()
                field_value = getattr(instance, field.name)

                field_node = ElementTree.SubElement(root, field.name)
                if field_type == 'DateTimeField':
                    field_node.text = field_value and field_value.strftime('%Y-%m-%d %H:%M:%S') or ''
                elif field_type == 'DateField':
                    field_node.text = field_value and field_value.strftime('%Y-%m-%d') or ''
                elif field_type == 'FileField' or field_type == 'ImageField':
                    field_node.text = field_value and field_value.url or ''
                elif field_type == 'ForeignKey':
                    fk_fields = field_type._meta.fields
                    for fk_field in fk_fields:
                        pass

                field_node.text = ''

        self.content = ''

