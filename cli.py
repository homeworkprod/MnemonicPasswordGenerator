#!/usr/bin/env python

"""cli.py

A command line interface to the Mnemonic Password Generator.

Copyright (c) 2004-2006 Jochen Kupperschmidt <webmaster@nwsnet.de>
Released under the terms of the GNU General Public License
  _                               _
 | |_ ___ _____ ___ _ _ _ ___ ___| |_
 |   | . |     | ._| | | | . |  _| . /
 |_|_|___|_|_|_|___|_____|___|_| |_|_\
   http://homework.nwsnet.de/
"""

from optparse import OptionParser

import mnemonicpasswords


def create_parser():
    parser = OptionParser(
        usage='%prog [options]',
        description='Generate pronounceable and thereby easier '
                    'remembered passwords.')

    parser.add_option('-l', '--letters',
        type='int',
        dest='letters',
        default=6,
        help='number of letters (default: 6)',
        metavar='NUM')

    parser.add_option('-d', '--digits',
        type='int',
        dest='digits',
        default=2,
        help='number of digits (default: 2)',
        metavar='NUM')

    parser.add_option('-u', '--uppercase',
        action='store_true',
        dest='uppercase',
        default=False,
        help='uppercase letters')

    parser.add_option('-p', '--passwords',
        type='int',
        dest='passwords',
        default=1,
        help='number of passwords to generate (default: 1)',
        metavar='NUM')

    return parser


def parse_options():
    parser = create_parser()

    options, args = parser.parse_args()
    if len(args):
        parser.print_help()
        parser.error('No arguments allowed; options only.')

    return options


def generate_passwords(total, letters, digits, uppercase):
    for i in range(options.passwords):
        yield mnemonicpasswords.generate_password(
            letters=options.letters,
            digits=options.digits,
            uppercase=options.uppercase)


if __name__ == '__main__':
    options = parse_options()

    passwords = generate_passwords(
        options.passwords,
        options.letters,
        options.digits,
        options.uppercase)

    for password in passwords:
        print password
