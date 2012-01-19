#!/usr/bin/env python
# -*- coding: utf-8 -*-
# <Couleur - fancy shell output for python>
# Copyright (C) <2010>  Gabriel Falcão <gabriel@nacaolivre.org>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
from setuptools import setup
import sys

extra = {}
if sys.version_info >= (3,0):
    u = str
    extra.update( use_2to3 = True )
else:
    u = lambda s: unicode(s, 'utf8')


setup(name='couleur',
    version=0.3,
    description='ANSI terminal tool for python, colored shell and other ' \
        'handy fancy features',
    author=u('Gabriel Falcão'),
    author_email='gabriel@nacaolivre.org',
    url='http://github.com/gabrielfalcao/couleur',
    py_modules=['couleur'],
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: Apache Software License',
        "Operating System :: POSIX",
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ],
    **extra
)
