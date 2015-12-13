# -*- coding: utf-8 -*-
# <Couleur - fancy shell output for python>
# Copyright (C) <2010-2012>  Gabriel Falcão <gabriel@nacaolivre.org>
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
import os
import re
import sys
import uuid
import platform

version = '0.6.2'

from StringIO import StringIO


class delimiters:
    DEFAULT = ("#{", "}")
    SQUARE_BRACKETS = ("[", "]")


SUPPORTS_ANSI = False
ANSI_OK = ('TERM' in os.environ and os.environ['TERM'] == 'ANSI')

for handle in [sys.stdout, sys.stderr]:
    if (hasattr(handle, "isatty") and handle.isatty()) or ANSI_OK:
        if platform.system() == 'Windows' and not ANSI_OK:
            SUPPORTS_ANSI = False
        else:
            SUPPORTS_ANSI = True

if os.getenv('COULEUR_DISABLE'):
    SUPPORTS_ANSI = False

if os.getenv('FORCE_COULEUR'):
    SUPPORTS_ANSI = True


def minify(string):
    regex_items = re.compile('(\033\[(\d+)m)')
    regex_main = re.compile('(?P<main>(\033\[(\d+)m){2,})')

    replaced = string
    main_found = regex_main.search(string)

    if main_found:
        existent = main_found.group('main')
        found = ";".join(x[1] for x in regex_items.findall(existent))
        if found:
            replaced = string.replace(existent, '\033[%sm' % found)

    return replaced


def wrapper_factory(delimiter):
    delimiter_in, delimiter_out = delimiter

    def wrap_escaped(middle_part):
        din = r"".join([r"\{0}".format(d) for d in delimiter_in])
        dout = r"".join([r"\{0}".format(d) for d in delimiter_out])
        return r"".join([din, middle_part, dout])

    def wrap_normal(middle_part):
        return r"".join([delimiter_in, middle_part, delimiter_out])

    return wrap_escaped, wrap_normal


def translate_colors(string, delimiter):
    wrap_escaped, wrap_normal = wrapper_factory(delimiter)

    for attr in re.findall(wrap_escaped("on[:](\w+)"), string):
        string = string.replace(
            wrap_normal(u"on:" + unicode(attr)),
            getattr(backcolors, attr)
        )

    for attr in re.findall(wrap_escaped("(\w+)"), string):
        string = string.replace(
            wrap_normal(attr),
            getattr(forecolors, attr, wrap_normal(attr))
        ).replace(
            wrap_normal(attr),
            getattr(modifiers, attr, wrap_normal(attr))
        )

    return minify(string)


def ignore_colors(string, delimiter):
    wrap_escaped, wrap_normal = wrapper_factory(delimiter)

    up_count_regex = re.compile(wrap_escaped(ur'up'))
    up_count = len(up_count_regex.findall(string)) or 1

    expression = (u'^(?P<start>.*)(' + wrap_escaped('up') + u')(.*\\n){%d}') % up_count
    up_supress_regex = re.compile(expression, re.MULTILINE)

    string = up_supress_regex.sub('\g<start>', string)

    for attr in re.findall(wrap_escaped("on[:](\w+)"), string):
        string = string.replace(wrap_normal(u"on:" + unicode(attr)), u"")

    for attr in re.findall(wrap_escaped("(\w+)"), string):
        string = (string
                  .replace(wrap_normal(attr), u"")
                  .replace(wrap_normal(attr), u""))

    return string


class Writer(StringIO):
    original = None
    translate = True

    def __init__(self, delimiter=delimiters.DEFAULT):
        self.delimiter = delimiter
        StringIO.__init__(self)

    def write(self, string):
        f = self.translate and translate_colors or ignore_colors
        self.original.write(f(string, self.delimiter))


class StdOutMocker(Writer):
    original = sys.__stdout__


class StdErrMocker(Writer):
    original = sys.__stderr__


class Proxy(object):
    def __init__(self, output, delimiter=delimiters.DEFAULT):
        self.old_write = output.write
        self.delimiter = delimiter

        if output is sys.__stdout__:
            output = StdOutMocker(delimiter)

        elif output is sys.__stderr__:
            output = StdErrMocker(delimiter)

        self.output = output

    def ignore(self):
        self.output.translate = False
        if not isinstance(self.output, (StdErrMocker, StdOutMocker)):
            self.output.write = lambda x: self.old_write(ignore_colors(x, self.delimiter))

    def enable(self):
        self.disable()

        self.output.translate = True
        if isinstance(self.output, StdOutMocker):
            sys.stdout = self.output
        elif isinstance(self.output, StdErrMocker):
            sys.stderr = self.output
        else:
            self.output.write = lambda x: self.old_write(translate_colors(x, self.delimiter))

    def disable(self):
        if isinstance(self.output, StdOutMocker):
            sys.stdout = self.output.original
        elif isinstance(self.output, StdErrMocker):
            sys.stderr = self.output.original
        else:
            self.output.write = self.old_write

_proxy_registry = {}


def proxy(output, delimiter=delimiters.DEFAULT):
    if output not in _proxy_registry.keys():
        _proxy_registry[output] = Proxy(output, delimiter)

    return _proxy_registry[output]


def ansify(number):
    """Wraps the given ansi code to a proper escaped python output

    Arguments:
    - `number`: the code in question
    """
    number = unicode(number)
    return u'\033[%sm' % number


class modifiers:
    reset = ansify(0)
    bold = ansify(1)
    blink = ansify(5)
    italic = ansify(3)
    underline = ansify(4)
    inverse = ansify(7)
    strikethrough = ansify(9)
    up = u'\r\033[A'


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


class empty(object):
    def __getattr__(self, attr):
        if attr != 'up':
            return u''
        else:
            return modifiers.up

_sep1 = u'_on_'
_sep2 = u'_and_'


class Shell(object):
    def __init__(self, output=None, indent=2, linebreak=False, bold=False,
                 disabled=not SUPPORTS_ANSI):
        self._indentation_factor = indent
        self._indent = 0
        self._linebreak = linebreak
        self._bold = bold
        self._in_format = False
        self._disabled = disabled
        self.output = output or sys.stdout

        if disabled:
            self._backcolors = empty()
            self._forecolors = empty()
            self._modifiers = empty()
        else:
            self._backcolors = backcolors()
            self._forecolors = forecolors()
            self._modifiers = modifiers()

    def indent(self):
        self._indent += self._indentation_factor

    def dedent(self):
        self._indent -= self._indentation_factor

    def _fore(self, color):
        def get(what):
            try:
                r = getattr(self._modifiers, what)
            except AttributeError:
                r = getattr(self._forecolors, what)
            return r

        args = map(get, color.split(u"_"))
        return u"".join(args)

    def _back(self, color):
        return getattr(self._backcolors, color)

    def _printer_for(self, color):
        colors = color.split(_sep1)

        parts = [
            self._fore(colors.pop(0)),
            u"%s",
            self._modifiers.reset
        ]

        if colors:
            parts.insert(0, self._back(colors[0]))

        if not self._in_format:
            if self._bold:
                parts.insert(0, self._modifiers.bold)

            if self._indent:
                parts.insert(0, u' ' * self._indent)

            if self._linebreak:
                parts.append(u"\n")

        string = u"".join(map(unicode, parts))

        def dec(z, replace=False):
            pre = unicode(replace and self._modifiers.up or u'')
            self.output.write(pre)
            self.output.write(string % unicode(z.decode('utf-8')))

        return dec

    def __getattr__(self, attr):
        if not attr.startswith(u"_"):
            if _sep2 in attr:
                self._in_format = True
                printers = map(self._printer_for, attr.split(_sep2))

                def dec(string, replace=False):
                    unique = str(uuid.uuid4())
                    string = string.replace(ur'\|', unique)
                    parts = string.split(ur"|")
                    if replace:
                        self.output.write(self._modifiers.up)

                    if self._indent:
                        self.output.write(u' ' * self._indent)

                    if self._bold:
                        self.output.write(self._modifiers.bold)

                    for part, output in zip(parts, printers):
                        output(part.replace(unique, ur"|"))

                    if self._linebreak:
                        self.output.write(u"\n")

                    self._in_format = False

                return dec

            return self._printer_for(attr)

        return super(Shell, self).__getattribute__(attr)
