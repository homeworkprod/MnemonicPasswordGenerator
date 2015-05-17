#!/usr/bin/env python

"""mnemonicpasswords.py -- Version 17-May-2015

Generate pronounceable and thereby easier remembered passwords despite of
their length.

Copyright (c) 2004-2006 Jochen Kupperschmidt <webmaster@nwsnet.de>
Released under the terms of the GNU General Public License
  _                               _
 | |_ ___ _____ ___ _ _ _ ___ ___| |_
 |   | . |     | ._| | | | . |  _| . /
 |_|_|___|_|_|_|___|_____|___|_| |_|_\
   http://homework.nwsnet.de/
"""

from random import choice, randrange


# Some consonants were left out for clarity or better pronunciation.
CHARSET = ('bdfghklmnprstvwz', 'aeiou') # consonants, vowels


def generate_password(letters=8, digits=4, uppercase=False):
    """Generate a random mnemonic password."""
    chars = ''.join(choice(CHARSET[i % 2]) for i in range(letters))
    if uppercase:
        chars = chars.upper()
    chars += ''.join(str(randrange(0, 9)) for i in range(digits))
    return chars


if __name__ == '__main__':
    print 'Generating sample passwords with alternating case:'
    for i in range(10):
        uppercase = i % 2
        print generate_password(uppercase=uppercase)
