#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from django.test import TestCase
from django.conf import settings
from odin.xml.models import ExampleModel
from odin.xml.exporter import XmlExporter

class XmlExporterTest(TestCase):

    fixtures = ['examplemodels.json']
    
    def test_xml_content(self):
        queryset = ExampleModel.objects.all()
        save_path = os.path.join(settings.MEDIA_ROOT, 'odin_tests')

        exporter = XmlExporter(queryset=queryset)
        exporter.save(save_dir=save_path, filename='odin_test.xml')

        content = exporter.content
        for instance in queryset:

            opts = instance._meta
            for field_name in opts.get_all_field_names():
                self.assertTrue(field_name in content)
                self.assertTrue(getattr(instance, field_name) in content)

        # remove the trash
        os.removedirs(save_path)
