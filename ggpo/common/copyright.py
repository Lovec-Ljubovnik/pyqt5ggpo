# -*- coding: utf-8 -*-

# define authorship information
__authors__ = ['papasi', ' pof', 'BridgetX']
__author__ = ','.join(__authors__)
__url__ = 'https://github.com/BridgetX/pyqt5ggpo'
__credits__ = [
    ('papasi',
     'https://github.com/doctorguile/pyqtggpo'),
    ('Tony Cannon (Ponder), Tom Cannon (ProtomCannon)',
     'http://ggpo.net'),
    ('Pau Oliva Fora (@pof)',
     'http://poliva.github.io/ggpo/'),
    ('BridgetX',
     'https://github.com/BridgetX/'),
]

__copyright__ = 'Copyright (c) 2014'
__license__ = 'GPL'

# define version information
__requires__ = ['PyQt5']
__version__ = 42


def versionString():
    return "{0:.2f}".format(__version__/100.0)


def versionNum():
    return __version__


def about():
    extra = '\n\nThis is a forked version of the FightCade client (by Pau Oliva - @pof) modified for PyQt5 by BridgetX.\nThe source code of this fork is available at https://github.com/BridgetX/pyqt5ggpo\n\n\n'
    for author, url in __credits__:
        extra += author + '\n' + url + "\n"
    return __copyright__ + ' ' + __author__ + "\n" + __url__ + "\n" + \
        'License: ' + __license__ + "\n" + \
        'Version: ' + versionString() + "\n" + \
        'Credits: ' + "\n" + extra
