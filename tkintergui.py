#!/usr/bin/env python

"""tkintergui.py -- Version 04-Feb-2006

A graphical frontend to the Mnemonic Password Generator in Tkinter.

Copyright (c) 2004-2006 Jochen Kupperschmidt <webmaster@nwsnet.de>
Released under the terms of the GNU General Public License
  _                               _
 | |_ ___ _____ ___ _ _ _ ___ ___| |_
 |   | . |     | ._| | | | . |  _| . /
 |_|_|___|_|_|_|___|_____|___|_| |_|_\
   http://homework.nwsnet.de/
"""

import Tkinter as tk

import mnemonicpasswords


class MnemonicPasswordFrame(tk.Frame):

    def __init__(self, master=None):
        """Initialize generator and populate frame."""
        tk.Frame.__init__(self, master)

        # Create and initialize variable wrappers.
        self.password = tk.StringVar()
        self.letterCount = tk.IntVar()
        self.letterCount.set(8)
        self.digitCount = tk.IntVar()
        self.digitCount.set(2)
        self.uppercase = tk.IntVar()

        # Create most controls.
        controls = [
            ('Password: ', tk.Entry(self,
                textvariable=self.password)),
            ('Letters:', NumberSlider(self,
                variable=self.letterCount,
                command=self.updatePassword)),
            ('Digits:', NumberSlider(self,
                variable=self.digitCount,
                command=self.updatePassword)),
            ('Case:', tk.Checkbutton(self,
                text='uppercase',
                variable=self.uppercase,
                command=self.updatePassword))
            ]
        for i in range(len(controls)):
            label, widget = controls[i]
            tk.Label(self,
                text=label
            ).grid(row=i, column=0, sticky=tk.W)
            widget.grid(row=i, column=1, sticky=tk.W)

        # Create refresh button.
        tk.Button(self,
            text='Generate another password',
            command=self.updatePassword
        ).grid(row=4, column=0, columnspan=2, sticky=tk.W+tk.E)

    def updatePassword(self, value=None):
        """Refresh password according to the current selection."""
        self.password.set(
            mnemonicpasswords.generateMnemonicPassword(
                self.letterCount.get(),
                self.digitCount.get(),
                self.uppercase.get()))


class NumberSlider(tk.Frame):
    """A slider showing the currently selected number on the side."""

    def __init__(self, master=None, variable=None, command=None):
        tk.Frame.__init__(self, master)
        tk.Label(self,
            textvariable=variable,
            width=2
        ).grid(row=0, column=0)
        tk.Scale(self,
            from_=0, to=16,
            orient=tk.HORIZONTAL,
            showvalue=0,
            variable=variable,
            command=command
        ).grid(row=0, column=1, sticky=tk.W+tk.E)


if __name__ == '__main__':
    app = MnemonicPasswordFrame()
    app.master.title('Mnemonic Password Generator')
    app.master.config(padx=2, pady=2)
    app.config(padx=4, pady=4, bd=2, relief=tk.GROOVE)
    app.grid(sticky=tk.N+tk.S+tk.W+tk.E)
    app.mainloop()
