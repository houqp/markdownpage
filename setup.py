#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

from distutils.core import setup

setup(name='markdownpage',
      version='',
      description='A program that generates html pages with template files and markdown files as input.',
      author='houqp',
      author_email='qingping.hou@gmail.com',
      url='https://github.com/houqp/markdownpage',
      download_url='https://github.com/houqp/markdownpage',
      license='GPL',
      packages=['markdownpage'],
      scripts=['scripts/mdpage'],
      )
