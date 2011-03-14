#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.db import models

class RelatedModel(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField(max_length=30)

    class Meta:
        verbose_name = 'related model'
        verbose_name_plural = 'related models'

    def __unicode__(self):
        return self.name


class ExampleModel(models.Model):
    char_field = models.CharField(max_length=50)
    datetime_field = models.DateTimeField()
    int_field = models.IntegerField()
    file_field = models.FileField(upload_to='odin_tests')
    fk_field = models.ForeignKey(RelatedModel, related_name='fk_fields')
    mm_field = models.ManyToManyField(RelatedModel, related_name='mm_fields')

    class Meta:
        verbose_name = 'example model'
        verbose_name_plural = 'example models'

    def __unicode__(self):
        return self.char_field

