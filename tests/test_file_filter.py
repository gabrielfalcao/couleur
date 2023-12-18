# -*- coding: utf-8 -*-
# <Couleur - fancy shell output for python>
# Copyright (C) <2010-2020>  Gabriel Falcão <gabriel@nacaolivre.org>
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
from io import StringIO

import couleur


def test_output_black_foreground():
    "file-like filter output: black foreground"

    io = StringIO()
    couleur.proxy(io).enable()
    io.write("#{black}Hello Black!\n")
    "\033[30mHello Black!\n".should.equal(io.getvalue())
    couleur.proxy(io).disable()
    io.seek(0)
    io.truncate()
    io.write("#{black}should not be translated\n")
    "#{black}should not be translated\n".should.equal(io.getvalue())


def test_output_black_on_white_foreground():
    "file-like filter output: black foreground on white background"

    io = StringIO()
    couleur.proxy(io).enable()
    io.write("#{black}#{on:white}Hello Black!\n")
    "\033[30;47mHello Black!\n".should.equal(io.getvalue())
    couleur.proxy(io).disable()
    io.seek(0)
    io.truncate()
    io.write("#{black}should not be translated\n")
    "#{black}should not be translated\n".should.equal(io.getvalue())


def test_output_green_foreground():
    "file-like filter output: green foreground"

    io = StringIO()
    couleur.proxy(io).enable()
    io.write("#{green}Hello Green!\n")
    "\033[32mHello Green!\n".should.equal(io.getvalue())
    couleur.proxy(io).disable()
    io.seek(0)
    io.truncate()
    io.write("#{black}should not be translated\n")
    "#{black}should not be translated\n".should.equal(io.getvalue())


def test_output_green_and_red_on_white_foreground():
    "file-like filter output: green foreground and white on red background"

    io = StringIO()
    couleur.proxy(io).enable()
    io.write("#{green}Hello #{white}#{on:red}Italy!\n")
    "\033[32mHello \033[37;41mItaly!\n".should.equal(io.getvalue())
    couleur.proxy(io).disable()
    io.seek(0)
    io.truncate()
    io.write("#{black}should not be translated\n")
    "#{black}should not be translated\n".should.equal(io.getvalue())


def test_output_bold_green_on_bold_white():
    "file-like filter output: bold green on white"

    io = StringIO()
    couleur.proxy(io).enable()
    io.write("#{bold}#{green}#{on:white}Hello\n")
    "\033[1;32;47mHello\n".should.equal(io.getvalue())
    couleur.proxy(io).disable()
    io.seek(0)
    io.truncate()
    io.write("#{black}should not be translated\n")
    "#{black}should not be translated\n".should.equal(io.getvalue())


def test_minify():
    "\033[1;32;41mHello\n".should.equal(couleur.minify("\033[1m\033[32m\033[41mHello\n"))
    "\033[1;32;41mHello\n".should.equal(couleur.minify("\033[1;32;41mHello\n"))


def test_ignoring_colors():
    "file-like filter output: ignoring output"

    io = StringIO()
    couleur.proxy(io).enable()
    couleur.proxy(io).ignore()
    io.write("#{bold}#{green}#{on:white}Hello\n")
    "Hello\n".should.equal(io.getvalue())
    couleur.proxy(io).disable()
    io.seek(0)
    io.truncate()
    io.write("#{black}should not be translated\n")
    "#{black}should not be translated\n".should.equal(io.getvalue())


def test_supress_up_when_ignoring_colors():
    "file-like filter output: supress #{up} when ignoring colors"

    io = StringIO()
    couleur.proxy(io).enable()
    couleur.proxy(io).ignore()
    io.write("This is visible#{up}but this is invisible\n")
    "This is visible".should.equal(io.getvalue())


def test_supress_up_when_ignoring_colors_as_many_times_needed():
    "file-like filter output: supress #{up} as many times as needed"

    io = StringIO()
    couleur.proxy(io).enable()
    couleur.proxy(io).ignore()
    io.write(
        "This is visible#{up}#{up}#{up}#{up}\n"
        " Line one supressed\n"
        " Line two supressed\n"
        " Line three supressed\n"
    )
    "This is visible".should.equal(io.getvalue())
