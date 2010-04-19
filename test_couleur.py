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
def test_mixed_output():
    "green_and_red_and_white is a valid call"
    sh = Shell()
    sh.green_and_red_and_white("Hello |World |for you!")
    assert_stdout(
        '\033[32mHello \033[0m\033[31mWorld \033[0m\033[37mfor you!\033[0m'
    )

@with_setup(prepare_stdout)
def test_mixed_output_with_escaped_separator():
    "green_and_red_on_yellow works is a valid call"
    sh = Shell()
    sh.green_and_red_on_yellow("Hello |World \|for you!")
    assert_stdout(
        '\033[32mHello \033[0m\033[43m\033[31mWorld |for you!\033[0m'
    )

@with_setup(prepare_stdout)
def test_mixed_output_with_backgrounds():
    "green_on_magenta_and_red_and_white_on_blue is a valid call"
    sh = Shell()
    sh.green_on_magenta_and_red_and_white_on_blue("Hello |World |for you!")
    assert_stdout('\033[45m\033[32mHello \033[0m\033[31mWorld \033[0m\033[44m\033[37mfor you!\033[0m'
    )

@with_setup(prepare_stdout)
def test_indent():
    "indentation"
    sh = Shell(indent=4, breakline=True)
    sh.normal_on_blue("Hello")
    sh.indent()
    sh.normal_on_red("World")
    assert_stdout('\033[44m\033[39mHello\033[0m\n    \033[41m\033[39mWorld\033[0m\n')

@with_setup(prepare_stdout)
def test_dedent():
    "de-indentation"
    sh = Shell(indent=4, breakline=True)
    sh.indent()
    sh.normal_on_blue("Hello")
    sh.dedent()
    sh.normal_on_red("World")
    assert_stdout('    \033[44m\033[39mHello\033[0m\n\033[41m\033[39mWorld\033[0m\n')

@with_setup(prepare_stdout)
def test_bold():
    "bold text"
    sh = Shell(bold=True)
    sh.normal_on_blue("Hello")
    sh.normal_on_red("World")
    assert_stdout('\033[1m\033[44m\033[39mHello\033[0m\033[1m\033[41m\033[39mWorld\033[0m')

@with_setup(prepare_stdout)
def test_bold_inline():
    "bold text with inline call"
    sh = Shell()
    sh.bold_normal_on_blue("Hello")
    sh.bold_normal_on_red("World")
    assert_stdout('\033[44m\033[1m\033[39mHello\033[0m\033[41m\033[1m\033[39mWorld\033[0m')

@with_setup(prepare_stdout)
def test_update_shell():
    "updating the shell, replacing the last output"
    sh = Shell(indent=6)
    sh.yellow("Yellow")
    sh.indent()
    sh.red("Red", True)
    assert_stdout('\033[33mYellow\033[0m\r\033[A      \033[31mRed\033[0m')

@with_setup(prepare_stdout)
def test_update_shell_mixed_with_linebreak():
    "updating the shell with mixed output and breakline enabled"
    sh = Shell(breakline=True)
    sh.yellow("Yellow")
    sh.yellow_and_normal_and_red("Yellow| and |Red", True)
    sh.green("Green")
    assert_stdout('\033[33mYellow\033[0m\n\r\033[A\033[33mYellow\033[0m\033[39m and \033[0m\033[31mRed\033[0m\n\033[32mGreen\033[0m\n')

@with_setup(prepare_stdout)
def test_update_shell_mixed_with_indentation():
    "updating the shell with mixed output and indentation"
    sh = Shell(breakline=True)
    sh.yellow("Yellow")
    sh.indent()
    sh.yellow_and_normal_and_red("Yellow| and |Red", True)
    sh.dedent()
    sh.green("Green")
    assert_stdout('\033[33mYellow\033[0m\n\r\033[A  \033[33mYellow\033[0m\033[39m and \033[0m\033[31mRed\033[0m\n\033[32mGreen\033[0m\n')

@with_setup(prepare_stdout)
def test_update_shell_mixed_with_bold():
    "updating the shell with mixed output and bold enabled"
    sh = Shell(bold=True)
    sh.yellow("Yellow")
    sh.yellow_and_normal_and_red("Yellow| and |Red", True)
    sh.green("Green")
    assert_stdout('\033[1m\033[33mYellow\033[0m\r\033[A\033[1m\033[33mYellow\033[0m\033[39m and \033[0m\033[31mRed\033[0m\033[1m\033[32mGreen\033[0m')
