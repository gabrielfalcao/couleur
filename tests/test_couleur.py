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
import sys
from io import StringIO
from sure import scenario, action_for, expect
from couleur import Shell


def prepare_output_stream(context):
    context.output = StringIO()

    @action_for(context, provides=["check_output"])
    def check_output(expected):
        context.output.getvalue().should.equal(expected)

    @action_for(context, provides=["check_output"])
    def make_shell(*args, **kw):
        context.sh = Shell(context.output, *args, **kw)


def test_default_output():
    "Shell.output should default to sys.stdout"
    sh = Shell()
    expect(sh.output).to.equal(sys.stdout)


@scenario(prepare_output_stream)
def test_output_black_foreground(spec):
    "Test output: black foreground"
    spec.make_shell()
    spec.sh.black("Hello Black!")
    spec.check_output("\033[30mHello Black!\033[0m")


@scenario(prepare_output_stream)
def test_output_black_foreground_on_white_background(spec):
    "Test output: black foreground on white background"
    spec.make_shell()
    spec.sh.black_on_white("Hello Black!")
    spec.check_output("\033[47m\033[30mHello Black!\033[0m")


@scenario(prepare_output_stream)
def test_output_green_foreground(spec):
    "Test output: green foreground"
    spec.make_shell()
    spec.sh.green("Hello World!")
    spec.check_output("\033[32mHello World!\033[0m")


@scenario(prepare_output_stream)
def test_mixed_output(spec):
    "green_and_red_and_white is a valid call"
    spec.make_shell()
    spec.sh.green_and_red_and_white("Hello |World |for you!")
    spec.check_output(
        "\033[32mHello \033[0m\033[31mWorld \033[0m\033[37mfor you!\033[0m"
    )


@scenario(prepare_output_stream)
def test_mixed_output_with_escaped_separator(spec):
    "green_and_red_on_yellow works is a valid call"
    spec.make_shell()
    spec.sh.green_and_red_on_yellow(r"Hello |World \|for you!")
    spec.check_output("\033[32mHello \033[0m\033[43m\033[31mWorld |for you!\033[0m")


@scenario(prepare_output_stream)
def test_mixed_output_with_backgrounds(spec):
    "green_on_magenta_and_red_and_white_on_blue is a valid call"
    spec.make_shell()
    spec.sh.green_on_magenta_and_red_and_white_on_blue("Hello |World |for you!")
    spec.check_output(
        "\033[45m\033[32mHello \033[0m\033[31mWorld \033[0m\033[44m\033[37mfor you!\033[0m"
    )


@scenario(prepare_output_stream)
def test_indent(spec):
    "indentation"
    spec.make_shell(indent=4, linebreak=True)
    spec.sh.normal_on_blue("Hello")
    spec.sh.indent()
    spec.sh.normal_on_red("World")
    spec.check_output(
        "\033[44m\033[39mHello\033[0m\n    \033[41m\033[39mWorld\033[0m\n"
    )


@scenario(prepare_output_stream)
def test_dedent(spec):
    "de-indentation"
    spec.make_shell(indent=4, linebreak=True)
    spec.sh.indent()
    spec.sh.normal_on_blue("Hello")
    spec.sh.dedent()
    spec.sh.normal_on_red("World")
    spec.check_output(
        "    \033[44m\033[39mHello\033[0m\n\033[41m\033[39mWorld\033[0m\n"
    )


@scenario(prepare_output_stream)
def test_bold(spec):
    "bold text"
    spec.make_shell(bold=True)
    spec.sh.normal_on_blue("Hello")
    spec.sh.normal_on_red("World")
    spec.check_output(
        "\033[1m\033[44m\033[39mHello\033[0m\033[1m\033[41m\033[39mWorld\033[0m"
    )


@scenario(prepare_output_stream)
def test_bold_inline(spec):
    "bold text with inline call"
    spec.make_shell()
    spec.sh.bold_normal_on_blue("Hello")
    spec.sh.bold_normal_on_red("World")
    spec.check_output(
        "\033[44m\033[1m\033[39mHello\033[0m\033[41m\033[1m\033[39mWorld\033[0m"
    )


@scenario(prepare_output_stream)
def test_update_shell(spec):
    "updating the shell, replacing the last output"
    spec.make_shell(indent=6)
    spec.sh.yellow("Yellow")
    spec.sh.indent()
    spec.sh.red("Red", True)
    spec.check_output("\033[33mYellow\033[0m\r\033[A      \033[31mRed\033[0m")


@scenario(prepare_output_stream)
def test_update_shell_mixed_with_linebreak(spec):
    "updating the shell with mixed output and linebreak enabled"
    spec.make_shell(linebreak=True)
    spec.sh.yellow("Yellow")
    spec.sh.yellow_and_normal_and_red("Yellow| and |Red", True)
    spec.sh.green("Green")
    spec.check_output(
        "\033[33mYellow\033[0m\n\r\033[A\033[33mYellow\033[0m\033[39m and \033[0m\033[31mRed\033[0m\n\033[32mGreen\033[0m\n"
    )


@scenario(prepare_output_stream)
def test_update_shell_mixed_with_indentation(spec):
    "updating the shell with mixed output and indentation"
    spec.make_shell(linebreak=True)
    spec.sh.yellow("Yellow")
    spec.sh.indent()
    spec.sh.yellow_and_normal_and_red("Yellow| and |Red", True)
    spec.sh.dedent()
    spec.sh.green("Green")
    spec.check_output(
        "\033[33mYellow\033[0m\n\r\033[A  \033[33mYellow\033[0m\033[39m and \033[0m\033[31mRed\033[0m\n\033[32mGreen\033[0m\n"
    )


@scenario(prepare_output_stream)
def test_update_shell_mixed_with_bold(spec):
    "updating the shell with mixed output and bold enabled"
    spec.make_shell(bold=True)
    spec.sh.yellow("Yellow")
    spec.sh.yellow_and_normal_and_red("Yellow| and |Red", True)
    spec.sh.green("Green")
    spec.check_output(
        "\033[1m\033[33mYellow\033[0m\r\033[A\033[1m\033[33mYellow\033[0m\033[39m and \033[0m\033[31mRed\033[0m\033[1m\033[32mGreen\033[0m"
    )


@scenario(prepare_output_stream)
def test_dont_print_colors_if_set_as_disabled(spec):
    "disable colors"
    spec.make_shell(disabled=True, linebreak=True, bold=True)
    spec.sh.yellow("Yellow")
    spec.sh.indent()
    spec.sh.indent()
    spec.sh.yellow_and_red_on_yellow("Yellow| and Red", True)
    spec.sh.dedent()
    spec.sh.green("Green")
    spec.check_output("Yellow\n\r\033[A    Yellow and Red\n  Green\n")
