#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

from setuptools import find_packages
import uuid
import imp

from pip.req import parse_requirements

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as f:
    readme = f.read()

# Avoiding import so we don't execute __init__.py, which has imports
# that aren't installed until after installation.
_meta = imp.load_source('_meta', 'rowpack/__meta__.py')

packages = find_packages()


install_requires = parse_requirements('requirements.txt', session=uuid.uuid1())

classifiers = [
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Software Development :: Libraries :: Python Modules',
]

setup(
    name='rowpack',
    version=_meta.__version__,
    description='Store row-oriented data in a msgpack format',
    long_description=readme,
    packages=packages,
    install_requires=[x for x in reversed([str(x.req) for x in install_requires])],
    author=_meta.__author__,
    author_email='eric@civicknowledge.com',
    url='https://github.com/CivicKnowledge/rowpack.git',
    license='MIT',
    classifiers=classifiers,
    entry_points={
        'console_scripts': [
            'rowpack=rowpack.cli:rowpack',
            'rpingest=rowpack.cli:rpingest',
            'mkmetatab=rowpack.cli:mkmetatab',
        ],
    },
)
