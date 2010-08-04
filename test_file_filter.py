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
from StringIO import StringIO
from nose.tools import assert_equals

import couleur

def test_output_black_foreground():
    "Test stderr filter output: black foreground"

    io = StringIO()
    couleur.proxy(io).enable()
    io.write("#{black}Hello Black!\n")
    assert_equals('\033[30mHello Black!\033[0m\n', io.getvalue())
    couleur.proxy(io).disable()
    io.seek(0)
    io.truncate()
    io.write("#{black}should not be translated\n")
    assert_equals('#{black}should not be translated\n', io.getvalue())

def test_output_black_on_white_foreground():
    "Test stderr filter output: black foreground on white background"

    io = StringIO()
    couleur.proxy(io).enable()
    io.write("#{black}#{on:white}Hello Black!\n")
    assert_equals('\033[30m\033[47mHello Black!\033[0m\n', io.getvalue())
    couleur.proxy(io).disable()
    io.seek(0)
    io.truncate()
    io.write("#{black}should not be translated\n")
    assert_equals('#{black}should not be translated\n', io.getvalue())

def test_output_green_foreground():
    "Test stderr filter output: green foreground"

    io = StringIO()
    couleur.proxy(io).enable()
    io.write("#{green}Hello Green!\n")
    assert_equals('\033[32mHello Green!\033[0m\n', io.getvalue())
    couleur.proxy(io).disable()
    io.seek(0)
    io.truncate()
    io.write("#{black}should not be translated\n")
    assert_equals('#{black}should not be translated\n', io.getvalue())

def test_output_green_and_red_on_white_foreground():
    "Test stderr filter output: green foreground and white on red background"

    io = StringIO()
    couleur.proxy(io).enable()
    io.write("#{green}Hello #{white}#{on:red}Italy!\n")
    assert_equals('\033[32mHello \033[37m\033[41mItaly!\033[0m\n', io.getvalue())
    couleur.proxy(io).disable()
    io.seek(0)
    io.truncate()
    io.write("#{black}should not be translated\n")
    assert_equals('#{black}should not be translated\n', io.getvalue())
