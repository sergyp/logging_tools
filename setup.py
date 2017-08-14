#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

import os


local_path = os.path.dirname(__file__)

with open('readme.rst') as _f:
    long_description = _f.read()

setup(
    name='logging_tools',
    version='0.0.1',
    author='Sergey Punkoff',
    author_email='svpmailbox@gmail.com',
    url='https://github.com/sergyp/logging_tools',
    download_url='https://github.com/sergyp/logging_tools/tarball/master'
    description='Simple cover of `logging` package to make configuring easy',
    long_description=long_description,
    classifiers=[
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: System :: Logging',
    ],
    packages=find_packages(),
    include_package_data=True,
    install_requires=[],
    py_modules = ['loigging_tools',]
)
