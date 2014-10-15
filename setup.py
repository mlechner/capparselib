#!/usr/bin/env python
"""
Build the capparselib module for parsing Common Alerting Protocol feeds.

"""
__author__ = 'kelvinn'
__version__ = '0.1'
__email__ = 'kelvin@kelvinism.com'

from distutils.core import setup

setup(name="capparselib",
    version="0.1",
    description="A module to parse and standardise CAP feeds",
    long_description="This module provides the ability to parse Common Alerting Protocol (CAP) feeds and standardise"
                     "the data into a dict, regardless if it was a 1.1 or 1.2 specification.",
    author="Kelvin Nicholson",
    author_email='kelvin@kelvinism.com',
    platforms = ['any'],
    package_dir = {'capparselib': 'src'},
    packages = ['capparselib']
)