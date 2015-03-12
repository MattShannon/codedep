#!/usr/bin/python
"""A setuptools-based script for distributing and installing codedep."""

# Copyright 2011, 2012, 2013, 2014 Matt Shannon

# This file is part of codedep.
# See `License` for details of license and warranty.


import os
from setuptools import setup

with open('README.rst') as readmeFile:
    long_description = readmeFile.read()

requires = [ line.rstrip('\n') for line in open('requirements.txt') ]

setup(
    name='codedep',
    version='0.4.dev1',
    description='Semi-automated code-level dependency tracking for python.',
    url='http://github.com/MattShannon/codedep',
    author='Matt Shannon',
    author_email='matt.shannon@cantab.net',
    license='3-clause BSD (see License file)',
    packages=['codedep'],
    install_requires=requires,
    scripts=[os.path.join('bin', 'codedep_check')],
    long_description=long_description,
)
