#!/usr/bin/env python

"""cli.py -- Version 04-Feb-2006

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


if __name__ == '__main__':
    # Create option parser and define options.
    parser = OptionParser(
        usage='%prog [options]',
        description='Generate pronounceable and thereby easier remembered passwords.')
    parser.add_option('-l', '--letters',
        type='int', dest='letters', default=6,
        help='number of letters (default: 6)', metavar='NUM')
    parser.add_option('-d', '--digits',
        type='int', dest='digits', default=2,
        help='number of digits (default: 2)', metavar='NUM')
    parser.add_option('-u', '--uppercase',
        action='store_true', dest='uppercase', default=False,
        help='uppercase letters')
    parser.add_option('-p', '--passwords',
        type='int', dest='passwords', default=1,
        help='number of passwords to generate (default: 1)', metavar='NUM')

    # Process options and arguments.
    (options, args) = parser.parse_args()
    if len(args):
        parser.print_help()
        parser.error('No arguments allowed, options only.')

    # Print passwords as requested.
    for i in range(options.passwords):
        print mnemonicpasswords.generateMnemonicPassword(
            letters=options.letters,
            digits=options.digits,
            uppercase=options.uppercase)
