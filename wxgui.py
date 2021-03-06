#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
A graphical frontend to the Mnemonic Password Generator in wxPython.

:Copyright: 2004-2015 `Jochen Kupperschmidt <http://homework.nwsnet.de/>`_
:License: GNU General Public License version 2, see LICENSE for details.
"""

import wx

import mnemonicpasswords


class ControlsPanel(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        # Create controls.
        self.password = wx.TextCtrl(self, style=wx.TE_READONLY)
        letterSliderPanel = SliderPanel(self, 8)
        self.letterCount = letterSliderPanel.slider
        digitSliderPanel = SliderPanel(self, 2)
        self.digitCount = digitSliderPanel.slider
        self.uppercase = wx.CheckBox(self, label='uppercase')
        controls = [
            ('Password', self.password),
            ('Letters', letterSliderPanel),
            ('Digits', digitSliderPanel),
            ('Case', self.uppercase)]
        button = wx.Button(self, label='Generate another password')

        # Add controls to sizer.
        sizer = wx.GridBagSizer(4, 4)
        for i in range(len(controls)):
            label, ctrl = controls[i]
            sizer.Add(wx.StaticText(self, label=label+':'), (i,0),
                flag=wx.ALIGN_LEFT|wx.ALIGN_CENTER_VERTICAL)
            sizer.Add(ctrl, (i,1), flag=wx.EXPAND)
        sizer.Add(button, (4,0), (1,2), flag=wx.EXPAND)
        sizer.AddGrowableCol(1)
        self.SetSizer(sizer)

        # Bind controls' events.
        self.letterCount.Bind(wx.EVT_SLIDER, self.on_settingsChange)
        self.digitCount.Bind(wx.EVT_SLIDER, self.on_settingsChange)
        self.uppercase.Bind(wx.EVT_CHECKBOX, self.on_settingsChange)
        button.Bind(wx.EVT_BUTTON, self.on_settingsChange)

        self.on_settingsChange()

    def on_settingsChange(self, evt=None):
        """Refresh password according to the current settings."""
        self.password.SetValue(
            mnemonicpasswords.generate_password(
                self.letterCount.GetValue(),
                self.digitCount.GetValue(),
                self.uppercase.GetValue()))
        if evt is not None:
            evt.Skip(True)


class SliderPanel(wx.Panel):

    def __init__(self, parent, value=2):
        wx.Panel.__init__(self, parent)

        # Create controls.
        self.label = wx.StaticText(self, label='00',
            style=wx.ALIGN_RIGHT|wx.ST_NO_AUTORESIZE)
        self.slider = wx.Slider(self, minValue=0, maxValue=10, value=value,
            style=wx.SL_AUTOTICKS)

        # Bind slider event.
        self.slider.Bind(wx.EVT_SLIDER, self.on_slide)

        # Arrange controls.
        sizer = wx.FlexGridSizer(1, 2, 4, 4)
        sizer.Add(self.label, flag=wx.ALIGN_CENTER)
        sizer.Add(self.slider, flag=wx.EXPAND)
        sizer.AddGrowableCol(1)
        self.SetSizer(sizer)

        self.on_slide(value)

    def on_slide(self, evt=None):
        self.label.SetLabel(str(self.slider.GetValue()))


class BorderPanel(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        sizer = wx.GridSizer()
        sizer.Add(ControlsPanel(self), flag=wx.EXPAND|wx.ALL, border=4)
        self.SetSizerAndFit(sizer)


class MainFrame(wx.Frame):

    def __init__(self):
        wx.Frame.__init__(self, None, title='Mnemonic Password Generator')

        sizer = wx.GridSizer()
        sizer.Add(BorderPanel(self), flag=wx.EXPAND)
        self.SetSizerAndFit(sizer)


if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = MainFrame()
    frame.Show()
    app.MainLoop()
