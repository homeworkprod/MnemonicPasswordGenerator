#!/usr/bin/env python

"""
Generate pronounceable and thereby easier remembered passwords despite of
their length.

:Copyright: 2004-2015 `Jochen Kupperschmidt <http://homework.nwsnet.de/>`_
:License: GNU General Public License version 2, see LICENSE for details.
"""

from itertools import chain
from random import choice, randrange


# Some consonants were left out for clarity or better pronunciation.
CONSONANTS = 'bdfghklmnprstvwz'
VOWELS = 'aeiou'


def generate_password(letters=8, digits=4, uppercase=False):
    """Generate a random mnemonic password."""
    chars = chain(_generate_letters(letters),
                  _generate_digits(digits))
    password = ''.join(chars)

    if uppercase:
        password = password.upper()

    return password


def _generate_letters(n):
    for i in range(n):
        source = CONSONANTS if (i % 2) == 0 else VOWELS
        yield choice(source)


def _generate_digits(n):
    for i in range(n):
        yield str(randrange(0, 9))


if __name__ == '__main__':
    print 'Generating sample passwords with alternating case:'
    for i in range(10):
        uppercase = i % 2
        print generate_password(uppercase=uppercase)
