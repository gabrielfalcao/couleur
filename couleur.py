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
import uuid

__version__ = '0.1'

def ansify(number):
    """Wraps the given ansi code to a proper escaped python output

    Arguments:
    - `number`: the code in question
    """
    number = unicode(number)
    return '\033[%sm' % number

class modifiers:
    reset = ansify(0)
    bold = ansify(1)
    blink = ansify(2)
    italic = ansify(3)
    underline = ansify(4)
    inverse = ansify(7)
    strikethrough = ansify(9)
    up = '\r\033[A'

    class off:
        bold = ansify(22)
        italic = ansify(23)
        underline = ansify(24)
        inverse = ansify(27)
        strikethrough = ansify(29)

class forecolors:
    black = ansify(30)
    red = ansify(31)
    green = ansify(32)
    yellow = ansify(33)
    blue = ansify(34)
    magenta = ansify(35)
    cyan = ansify(36)
    white = ansify(37)
    normal = ansify(39)

class backcolors:
    black = ansify(40)
    red = ansify(41)
    green = ansify(42)
    yellow = ansify(43)
    blue = ansify(44)
    magenta = ansify(45)
    cyan = ansify(46)
    white = ansify(47)
    normal = ansify(49)

def fore(color):
    def get(what):
        try:
            r = getattr(modifiers, what)
        except AttributeError:
            r = getattr(forecolors, what)
        return r

    args = map(get, color.split("_"))
    return "".join(args)

def back(color):
    return getattr(backcolors, color)

_sep1 = '_on_'
_sep2 = '_and_'

class Shell(object):
    def __init__(self, indent=2, breakline=False, bold=False):
        self._indentation_factor = indent
        self._indent = 0
        self._breakline = breakline
        self._bold = bold
        self._in_format = False

    def indent(self):
        self._indent += self._indentation_factor

    def dedent(self):
        self._indent -= self._indentation_factor

    def _printer_for(self, color):
        colors = color.split(_sep1)

        parts = [
            fore(colors.pop(0)),
            "%s",
            modifiers.reset
        ]

        if colors:
            parts.insert(0, back(colors[0]))

        if not self._in_format:
            if self._bold:
                parts.insert(0, ansify(1))

            if self._indent:
                parts.insert(0, ' ' * self._indent)

            if self._breakline:
                parts.append("\n")

        string = "".join(parts)

        def dec(z, replace=False):
            pre = (replace and modifiers.up or '')
            sys.stdout.write(pre + (string % z))

        return dec


    def __getattr__(self, attr):
        if not attr.startswith("_"):
            if _sep2 in attr:
                self._in_format = True
                printers = map(self._printer_for, attr.split(_sep2))
                def dec(string, replace=False):
                    unique = str(uuid.uuid4())
                    string = string.replace(r'\|', unique)
                    parts = string.split("|")
                    if replace:
                        sys.stdout.write(modifiers.up)

                    if self._indent:
                        sys.stdout.write(' ' * self._indent)

                    if self._bold:
                        sys.stdout.write(ansify(1))

                    for part, output in zip(parts, printers):
                        output(part.replace(unique, "|"))

                    if self._breakline:
                        sys.stdout.write("\n")

                    self._in_format = False

                return dec

            return self._printer_for(attr)

        return super(Shell, self).__getattribute__(attr)
