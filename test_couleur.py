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

from couleur import ansify
from couleur import Shell

def prepare_stdout():
    if isinstance(sys.stdout, StringIO):
        del sys.stdout

    std = StringIO()
    sys.stdout = std

def assert_stdout(expected):
    string = sys.stdout.getvalue()
    assert_equals(string, expected)

def test_ansify():
    "couleur.ansify wraps ansi code for proper pythonic output"
    assert_equals(ansify(0), '\033[0m')

@with_setup(prepare_stdout)
def test_output_black_foreground():
    "Test output: black foreground"
    sh = Shell()
    sh.black("Hello Black!")
    assert_stdout('\033[30mHello Black!\033[0m')

@with_setup(prepare_stdout)
def test_output_black_foreground_on_white_background():
    "Test output: black foreground on white background"
    sh = Shell()
    sh.black_on_white("Hello Black!")
    assert_stdout('\033[47m\033[30mHello Black!\033[0m')

@with_setup(prepare_stdout)
def test_output_green_foreground():
    "Test output: green foreground"
    sh = Shell()
    sh.green("Hello World!")
    assert_stdout('\033[32mHello World!\033[0m')

@with_setup(prepare_stdout)
def _test_mixed_output():
    sh = Shell()
    sh.green_and_red_and_white("Hello |World |for you!")
    assert_stdout(
        '\033[32mHello \033[0m\033[31mWorld \033[0m\033[37mfor you!\033[0m'
    )

@with_setup(prepare_stdout)
def _test_mixed_output_with_escaped_separator():
    sh = Shell()
    sh.green_and_red_on_yellow("Hello |World \|for you!")
    assert_stdout(
        '\033[32mHello \033[0m\033[43m\033[31mWorld for you!\033[0m'
    )

@with_setup(prepare_stdout)
def _test_mixed_output_with_backgrounds():
    sh = Shell()
    sh.green_on_magenta_and_red_and_white_on_blue("Hello |World |for you!")
    assert_stdout('\033[45m\033[32mHello \033[0m\033[31mWorld \033[0m\033[44m\033[37mfor you!\033[0m'
    )
