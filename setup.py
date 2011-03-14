#!/usr/bin/env python
#-*- coding: utf-8 -*-
from distutils.core import setup

VERSION = '0.1'

setup = setup(
    name='django-odin',
    version=VERSION,
    description=u'Tools for django developers',
    author='Heigler Rocha',
    author_email='lordheigler@gmail.com',
    platforms=['any'],
    packages=[
        'odin',
    ]
)

