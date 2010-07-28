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
import sys
from StringIO import StringIO
from nose.tools import with_setup, assert_equals

import couleur

def prepare_stdout():
    if isinstance(sys.stdout, StringIO):
        del sys.stdout

    std = StringIO()
    sys.stdout = std

def assert_stdout(expected):
    string = sys.stdout.getvalue()
    assert_equals(string, expected)

@with_setup(prepare_stdout)
def test_output_black_foreground():
    "Test stdout filter output: black foreground"

    couleur.proxy(sys.stdout).enable()
    print "#{black}Hello Black!"
    assert_stdout('\033[30mHello Black!\033[0m\n')
    couleur.proxy(sys.stdout).disable()

@with_setup(prepare_stdout)
def test_output_black_on_white_foreground():
    "Test stdout filter output: black foreground on white background"

    couleur.proxy(sys.stdout).enable()
    print "#{black}#{on:white}Hello Black!"
    assert_stdout('\033[30m\033[47mHello Black!\033[0m\n')
    couleur.proxy(sys.stdout).disable()

@with_setup(prepare_stdout)
def test_output_green_foreground():
    "Test stdout filter output: green foreground"

    couleur.proxy(sys.stdout).enable()
    print "#{green}Hello Green!"
    assert_stdout('\033[32mHello Green!\033[0m\n')
    couleur.proxy(sys.stdout).disable()

@with_setup(prepare_stdout)
def test_output_green_and_red_on_white_foreground():
    "Test stdout filter output: green foreground and white on red background"

    couleur.proxy(sys.stdout).enable()
    print "#{green}Hello #{white}#{on:red}Italy!"
    assert_stdout('\033[32mHello \033[37m\033[41mItaly!\033[0m\n')
    couleur.proxy(sys.stdout).disable()

