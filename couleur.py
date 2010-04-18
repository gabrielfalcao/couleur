# -*- coding: utf-8 -*-
# <Couleur - fancy shell output for python>
# Copyright (C) <2010>  Gabriel Falcão <gabriel@nacaolivre.org>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import sys

# [0m  -> reset
# [1m  -> bold on
# [3m  -> italics on
# [4m  -> underline on
# [7m  -> inverse on
# [9m  -> strikethrough on
# [22m -> bold off
# [23m -> italics off
# [24m -> underline off
# [27m -> inverse off
# [29m -> strikethrough off
# [30m -> fore color black
# [31m -> fore color red
# [32m -> fore color green
# [33m -> fore color yellow
# [34m -> fore color blue
# [35m -> fore color magenta
# [36m -> fore color cyan
# [37m -> fore color white
# [39m -> fore color default
# [40m -> back color black
# [41m -> back color red
# [42m -> back color green
# [43m -> back color yellow
# [44m -> back color blue
# [45m -> back color magenta
# [46m -> back color cyan
# [47m -> back color white
# [49m -> back color default

def ansify(number):
    """Wraps the given ansi code to a proper escaped python output

    Arguments:
    - `number`: the code in question
    """
    number = unicode(number)
    return '\033[%sm' % number

class Shell(object):
    def black(self, string):
        sys.stdout.write(ansify(30) + string + ansify(0))

    def black_on_white(self, string):
        sys.stdout.write(ansify(47) + ansify(30) + string + ansify(0))

    def green(self, string):
        sys.stdout.write(ansify(32) + string + ansify(0))

