#! /usr/bin/env python
# -*- coding: utf-8

import os
import sys

from setuptools import setup, find_packages

import crunch

def publish():
    """ publish to pypi """
    os.system("python setup.py sdist upload")

if sys.argv[-1] == "publish":
    publish()
    sys.exit()

required = ['requests', 'client', 'gevent']

setup(
    name = 'crunch',
    version = crunch.__version__,
    description = 'Command line tool download and upload files',
    long_description = open('README.rst').read() + '\n\n' ,
    author = 'kracekumar',
    author_email = 'me@kracekumar.com',
    url = "https://github.com/kracekumar/crunch",
    data_files = [
        'README.rst',
        ],
    packages = find_packages(),
    install_required = required,
    tests_require = ['nose'],
    entry_point = {
        'console_scripts': ['crunch = crunch.core.main',]
        },
    license = 'ISC',
    classifiers = (
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: System Administrators',
        'Natural Language :: English',
        'License :: OSI Approved :: ISC License (ISCL)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Terminals :: Terminal Emulators/X Terminals',
        ),
    )
