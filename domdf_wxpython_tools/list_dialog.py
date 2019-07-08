#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  list_dialog.py
#
#  Copyright 2019 Dominic Davis-Foster <dominic@davis-foster.co.uk>
#
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published by
#  the Free Software Foundation; either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
#
# generated by wxGlade 0.9.3 on Wed Jun 12 18:14:39 2019
#

import wx
# begin wxGlade: dependencies
# end wxGlade

# begin wxGlade: extracode
# end wxGlade


class list_dialog(wx.Dialog):
    def __init__(self, parent, title="Choose", label="Choose: ",
                 choices=None, *args, **kwds):
        if choices is None:
            choices = ["egg and bacon",
                       "egg sausage and bacon",
                       "egg and spam",
                       "egg bacon and spam",
                       "egg bacon sausage and spam",
                       "spam bacon sausage and spam",
                       "spam egg spam spam bacon and spam",
                       "spam sausage spam spam bacon spam tomato and spam",
                       "spam spam spam egg and spam",
                       "spam spam spam spam spam spam baked beans spam spam spam",
                       ]
        self.title = title
        self.label = label
        self.choices = choices

        args = (parent,) + args
        # begin wxGlade: list_dialog.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_DIALOG_STYLE
        wx.Dialog.__init__(self, *args, **kwds)
        self.SetSize((512, -1))
        self.main_panel = wx.Panel(self, wx.ID_ANY)
        self.list_box = wx.ListBox(self.main_panel, wx.ID_ANY, choices=[])
        self.cancel_btn = wx.Button(self.main_panel, wx.ID_CANCEL, "")
        self.select_btn = wx.Button(self.main_panel, wx.ID_ANY, "Select")

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_LISTBOX_DCLICK, self.do_select, self.list_box)
        self.Bind(wx.EVT_BUTTON, self.do_select, self.select_btn)
        # end wxGlade
        self.list_box.Clear()
        self.list_box.AppendItems(choices)

    def __set_properties(self):
        # begin wxGlade: list_dialog.__set_properties
        self.SetTitle("Choose")
        self.SetSize((512, -1))
        # end wxGlade
        self.SetTitle(self.title)

    def __do_layout(self):
        # begin wxGlade: list_dialog.__do_layout
        parent_sizer = wx.BoxSizer(wx.VERTICAL)
        main_sizer = wx.BoxSizer(wx.VERTICAL)
        btn_sizer = wx.GridSizer(1, 2, 0, 7)
        borders_label = wx.StaticText(self.main_panel, wx.ID_ANY, "Choose: ")
        borders_label.SetFont(wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, 0, ""))
        main_sizer.Add(borders_label, 0, wx.BOTTOM, 7)
        main_sizer.Add(self.list_box, 1, wx.EXPAND, 0)
        static_line_10 = wx.StaticLine(self.main_panel, wx.ID_ANY)
        main_sizer.Add(static_line_10, 0, wx.BOTTOM | wx.EXPAND | wx.TOP, 5)
        btn_sizer.Add(self.cancel_btn, 0, wx.ALIGN_CENTER, 0)
        btn_sizer.Add(self.select_btn, 0, wx.ALIGN_CENTER, 0)
        main_sizer.Add(btn_sizer, 0, wx.ALIGN_BOTTOM | wx.ALIGN_RIGHT, 0)
        self.main_panel.SetSizer(main_sizer)
        parent_sizer.Add(self.main_panel, 1, wx.ALL | wx.EXPAND, 10)
        self.SetSizer(parent_sizer)
        self.Layout()
        # end wxGlade
        borders_label.SetLabel(self.label)

    def do_select(self, event):  # wxGlade: list_dialog.<event_handler>
        self.EndModal(wx.ID_OK)

    def do_cancel(self, event):  # wxGlade: list_dialog.<event_handler>
        self.Destroy()

# end of class list_dialog