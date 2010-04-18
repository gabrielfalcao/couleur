# couleur - colored terminal tool for python
> Version 0.1

## Nutshell

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

# Nomenclature:

  "couleur" stands for "color" in French, I like french, hence the name

# Licensing

    Copyright (c) 2010 Gabriel Falcão
    Licensed under LGPL 3+
    http://www.gnu.org/copyleft/gpl.html
