Mnemonic Password Generator
===========================

Generate pronounceable and thereby easier remembered passwords despite
of their length.

:Copyright: 2004-2015 `Jochen Kupperschmidt <http://homework.nwsnet.de/>`_
:Date: 09-Jun-2015 (original release: 27-Jul-2004)
:License: GNU General Public License version 2, see LICENSE for details.
:Version: 0.1.1

::

     _                               _
    | |_ ___ _____ ___ _ _ _ ___ ___| |_
    |   | . |     | ._| | | | . |  _| . /
    |_|_|___|_|_|_|___|_____|___|_| |_|_\
      http://homework.nwsnet.de/


Requirements
------------

- Python_ (tested with version 2.3.5)
- [optional, for the Tk_ GUI] Tkinter_ (included with Python, at least
  on Windows)
- [optional, for the wxWidgets_ GUI] wxPython_ (tested with version
  2.6.1.0)


Files
-----

``cli.py``
    A command line interface.

``mnemonicpasswords.py``
    The core module that provides the password generation functionality.

``README.rst``
    This text.

``tkintergui.py``
    A graphical user interface written in Tkinter_.

``wxgui.py``
    A graphical user interface written in wxPython_.


.. _Python:    http://www.python.org/
.. _Tk:        http://www.tcl.tk/
.. _Tkinter:   https://wiki.python.org/moin/TkInter
.. _wxWidgets: http://www.wxwidgets.org/
.. _wxPython:  http://www.wxpython.org/
