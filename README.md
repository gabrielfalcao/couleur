# couleur - ANSI terminal tool for python, colored shell and other handy fancy features
__Version 0.1__

__Couleur__ is a handy tool to play around with ANSI features in a
unix terminal

## features

+ Single python file
+ 100% tested
+ comes with syntax sugar

## nutshell

couleur has a syntax sugar that is semantically nice:

    import couleur
    sh = couleur.Shell(indent=4)

    sh.bold_black_on_white('Nice highlight')
    # prints '\033[1m\033[47m\033[30mNice highlight\033[0m'

    sh.indent()
    # will increase a internal indentation factor in couleur.Shell instance

    sh.green('Just green')
    # prints indented as well '    \033[32mJust Green\033[0m'

    sh.dedent()
    # will decrease that indentation factor (above)

    # syntax sugar
    sh.green_and_nornal_and_blue('this will be printed in green| and |this in blue')
    # see: '\033[32mthis will be printed in green\033[0m and \033[34mthis in blue\033[0m'

## free software

To contribute back with this project, all you need to do is write code, and test code that proofs its functionallity

### cloning and running tests

You will need to install [nose](http://somethingaboutorange.com/mrl/projects/nose/0.11.3/ "a pretty way for testing in python").

And run:
    user@machine:~/Projects$ git clone git://github.com/gabrielfalcao/couleur.git
    user@machine:~/Projects$ cd couleur
    user@machine:~/Projects/couleur$ nosetests

## nomenclature

  "couleur" stands for "color" in French, I like french, hence the name

## Licensing

    Copyright (c) 2010 Gabriel Falcão
    Licensed under LGPL 3+
    http://www.gnu.org/copyleft/gpl.html
