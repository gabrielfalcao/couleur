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
    italic = ansify(3)
    underline = ansify(4)
    inverse = ansify(7)
    strikethrough = ansify(9)

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
    default = ansify(39)

class backcolors:
    black = ansify(40)
    red = ansify(41)
    green = ansify(42)
    yellow = ansify(43)
    blue = ansify(44)
    magenta = ansify(45)
    cyan = ansify(46)
    white = ansify(47)
    default = ansify(49)

def fore(color):
    return getattr(forecolors, color)

def back(color):
    return getattr(backcolors, color)

_sep1 = '_on_'
_sep2 = '_and_'

def _printer_for(color):
    colors = color.split(_sep1)

    parts = [
        fore(colors.pop(0)),
        "%s",
        modifiers.reset
    ]

    if colors:
        parts.insert(0, back(colors[0]))

    string = "".join(parts)
    return lambda z: sys.stdout.write(string % z)

class Shell(object):
    def __getattr__(self, attr):
        if _sep2 in attr:
            printers = map(_printer_for, attr.split(_sep2))
            def dec(string):
                unique = str(uuid.uuid4())
                string = string.replace(r'\|', unique)
                parts = string.split("|")

                for part, output in zip(parts, printers):
                    output(part.replace(unique, "|"))
            return dec

        try:
            return _printer_for(attr)
        except AttributeError:
            return super(Shell, self).__getattribute__(attr)
