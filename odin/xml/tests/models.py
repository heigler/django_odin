#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import datetime
from django.test import TestCase
from odin.xml.models import ExampleModel, RelatedModel

class RelatedModelTest(TestCase):

    def test_creation(self):
        instance = RelatedModel.objects.create(name='related', slug='related')
        self.assertEqual(RelatedModel.objects.count(), 1)     


class ExampleModelTest(TestCase):

    fixtures = ['relatedmodels.json']

    def test_creation(self):
        now = datetime.now()
        related_instance = RelatedModel.objects.all()[0]
        instance = ExampleModel.objects.create(char_field='test string', datetime_field=now, int_field=14,
                                               file_field='test.mp3', fk_field=related_instance)
        instance.mm_field.add(related_instance)

        self.assertEqual(ExampleModel.objects.count(), 1)
