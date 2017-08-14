#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

import os


local_path = os.path.dirname(__file__)

with open('readme.rst') as _f:
    description = _f.read()

setup(
    name='logging_tools',
    version='0.0.1',
    author='Sergey Punkoff',
    url='',
    description=description,
    author_email='svpmailbox@gmail.com',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[],
    py_modules = ['loigging_tools',]
)
