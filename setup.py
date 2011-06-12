#!/usr/bin/env python

import os

from distutils.core import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='flameforged',
    version='0.0.1',
    description='flameforged is a set of tools I use for django app development',
    author='Chris \'Wraithan\' McDonald',
    author_email='xwraithanx@gmail.com',
    url='http://api.flameforged.org',
    packages=('flameforged',), 
    long_description=read('README'),
    requires=('django'),
    classifiers=(
          'Development Status :: 3 - Alpha',
          'Environment :: Console',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: BSD License',
          'Operating System :: MacOS :: MacOS X',
          'Operating System :: Unix',
          'Operating System :: POSIX',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',
          'Topic :: Software Development',
          'Topic :: Software Development :: Libraries',
          'Topic :: Software Development :: Libraries :: Python Modules',
    ),
)
