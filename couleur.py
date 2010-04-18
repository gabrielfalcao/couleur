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

class Shell(object):
    def black(self, string):
        sys.stdout.write(forecolors.black + string + modifiers.reset)

    def black_on_white(self, string):
        sys.stdout.write(backcolors.white + forecolors.black + string + modifiers.reset)

    def green(self, string):
        sys.stdout.write(forecolors.green + string + modifiers.reset)
