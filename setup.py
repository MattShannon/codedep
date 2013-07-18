#!/usr/bin/python
"""A distutils-based script for distributing and installing codedep."""

# Copyright 2011, 2012, 2013 Matt Shannon

# This file is part of codedep.
# See `License` for details of license and warranty.


from distutils.core import setup

with open('README.rst') as readmeFile:
    long_description = readmeFile.read()

setup(
    name = 'codedep',
    version = '0.3',
    description = 'Semi-automated code-level dependency tracking for python.',
    url = 'http://github.com/MattShannon/codedep',
    author = 'Matt Shannon',
    author_email = 'matt.shannon@cantab.net',
    license = '3-clause BSD (see License file)',
    packages = ['codedep'],
    scripts = ['bin/codedep_check'],
    long_description = long_description,
)
