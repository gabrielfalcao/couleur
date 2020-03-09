couleur - ANSI terminal tool for python, colored shell and other handy fancy features
=====================================================================================
.. image:: https://img.shields.io/pypi/dm/couleur
   :target: https://pypi.org/project/couleur

.. image:: https://img.shields.io/codecov/c/github/gabrielfalcao/couleur
   :target: https://codecov.io/gh/gabrielfalcao/couleur

.. image:: https://img.shields.io/github/workflow/status/gabrielfalcao/couleur/python-3.6?label=python%203.6
   :target: https://github.com/gabrielfalcao/couleur/actions

.. image:: https://img.shields.io/github/workflow/status/gabrielfalcao/couleur/python-3.7?label=python%203.7
   :target: https://github.com/gabrielfalcao/couleur/actions

.. image:: https://img.shields.io/readthedocs/couleur
   :target: https://couleur.readthedocs.io/

.. image:: https://img.shields.io/github/license/gabrielfalcao/couleur?label=Github%20License
   :target: https://github.com/gabrielfalcao/couleur/blob/master/LICENSE

.. image:: https://img.shields.io/pypi/v/couleur
   :target: https://pypi.org/project/couleur

.. image:: https://img.shields.io/pypi/l/couleur?label=PyPi%20License
   :target: https://pypi.org/project/couleur

.. image:: https://img.shields.io/pypi/format/couleur
   :target: https://pypi.org/project/couleur

.. image:: https://img.shields.io/pypi/status/couleur
   :target: https://pypi.org/project/couleur

.. image:: https://img.shields.io/pypi/pyversions/couleur
   :target: https://pypi.org/project/couleur

.. image:: https://img.shields.io/pypi/implementation/couleur
   :target: https://pypi.org/project/couleur

.. image:: https://img.shields.io/snyk/vulnerabilities/github/gabrielfalcao/couleur
   :target: https://github.com/gabrielfalcao/couleur/network/alerts

.. image:: https://img.shields.io/github/v/tag/gabrielfalcao/couleur
   :target: https://github.com/gabrielfalcao/couleur/releases


**Couleur** is a handy tool to play around with ANSI features in a unix
terminal

installing
----------

::

   user@machine:~$ sudo pip install git+git://github.com/gabrielfalcao/couleur.git

features
--------

-  Single python file
-  100% tested
-  comes with syntax sugar

nutshell
--------

file-like objects filter
~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: http://gnu.gabrielfalcao.com/couleur_filter.png
   :alt: stdout filter

   stdout filter

further
^^^^^^^

.. code:: python

   import sys, couleur

   couleur.proxy(sys.stdout).enable()
   print "#{bold}#{blue}#{on:black}This is#{normal} a test"
   couleur.proxy(sys.stdout).ignore()

   print "#{green}#{on:black}This is#{normal} a test"
   couleur.proxy(sys.stdout).disable()

dynamic methods
~~~~~~~~~~~~~~~

couleur has a syntax sugar that is semantically nice:

.. code:: python

   print
   import couleur
   sh = couleur.Shell(indent=4)

   sh.bold_black_on_white('Nice highlight\n')
   # prints '\033[47m\033[1m\033[30mNice highlight\033[0m'

   sh.indent()
   # will increase a internal indentation factor in couleur.Shell instance

   sh.red('Just red\n')
   # prints indented as well '    \033[32mJust Green\033[0m\n'

   sh.dedent()

   # will decrease that indentation factor (above)

   # syntax sugar
   sh.green_and_normal_and_blue('this will be printed in green| and |this in blue\n')
   # see: '\033[32mthis will be printed in green\033[0m and \033[34mthis in blue\033[0m'

couleur can overwrite output, so that you can make things like printing
progress bars, show percentage and so on:

.. code:: python

   import time
   import couleur

   shell = couleur.Shell(linebreak=True, bold=True)

   for num in range(101):
       if num == 0:
           print

       shell.yellow_and_red("Downloading file: |%d%%" % num, replace=True)
       time.sleep(0.02)

   shell.white_and_green("Downloading file: |DONE!", replace=True)

Writing to other streams
^^^^^^^^^^^^^^^^^^^^^^^^

Simply pass the output as first argument of the ``Shell``

.. code:: python

   import couleur

   with open('output.log', 'w') as output:
       shell = couleur.Shell(output, linebreak=True, bold=True)
       shell.white_and_green("done with | Some task")

furthermore
~~~~~~~~~~~

With couleur you can mix modifiers and colors.

Available modifiers:

-  reset - resets from the current point to the end
-  bold - make text bold
-  blink - it may blink the text or make it slighly lighten, depending
   on the terminal
-  italic - make text italic
-  underline - add underline on text
-  inverse - invert colors
-  strikethrough - draws a line through the text
-  up - does the same than passing replace=True to the output function:
   carriage return and one line up

Available colors:

-  normal
-  black
-  red
-  green
-  yellow
-  blue
-  magenta
-  cyan
-  white

Example chaining modifiers:

.. code:: python

   import couleur

   shell = couleur.Shell(linebreak=True)
   shell.bold_italic_underline_green_on_black_and_italic_black_on_white("WOO| HOO")

free software
-------------

To contribute back with this project, all you need to do is write code,
and test code that proofs its functionallity

cloning and running tests
~~~~~~~~~~~~~~~~~~~~~~~~~

You will need to install
`nose <http://somethingaboutorange.com/mrl/projects/nose/0.11.3/>`__.

And run:

.. code:: shell

   user@machine:~/Projects$ git clone git://github.com/gabrielfalcao/couleur.git
   user@machine:~/Projects$ cd couleur
   user@machine:~/Projects/couleur$ make tests

nomenclature
------------

“couleur” stands for “color” in French, I like french, hence the name

Licensing
---------

::

   Copyright (c) 2010-2020 Gabriel Falcão
   Licensed under Apache License 2.0
   http://www.apache.org/licenses/LICENSE-2.0.html

`Bitdeli Badge <https://bitdeli.com/free>`__
