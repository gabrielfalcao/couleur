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
import couleur
from setuptools import setup, find_packages

setup(name='couleur',
    version=couleur.__version__,
    description='ANSI terminal tool for python, colored shell and other ' \
        'handy fancy features',
    author=u'Gabriel Falcão',
    author_email='gabriel@nacaolivre.org',
    py_modules=['couleur'],
)
