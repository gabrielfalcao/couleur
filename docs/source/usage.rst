Usage
=====

::

    import sys
    import couleur

    couleur.proxy(sys.stdout).enable()
    print "#{bold}#{blue}#{on:black}This is#{normal} a test"
    couleur.proxy(sys.stdout).ignore()

    print "#{green}#{on:black}This is#{normal} a test"
    couleur.proxy(sys.stdout).disable()
