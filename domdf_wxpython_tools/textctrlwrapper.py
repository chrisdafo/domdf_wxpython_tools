#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  textctrlwrapper.py
#
#  Copyright 2019-2020 Dominic Davis-Foster <dominic@davis-foster.co.uk>
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
# generated by wxGlade 0.9.3 on Thu Jun  6 12:07:28 2019
#

# TODO: Forward events
from typing import Tuple

# 3rd party
import wx  # type: ignore

# stdlib

class TextCtrlWrapper:
	"""
	Must set the value of self.textctrl
	"""

	textctrl: wx.TextCtrl

	def AppendText(self, text: str):
		"""
		Appends the text to the end of the text control.

		:param text: Text to write to the text control
		:type text: string
		"""

		return self.textctrl.AppendText(text)

	def CanCopy(self) -> float:
		"""
		Returns True if the selection can be copied to the clipboard.

		:rtype: bool
		"""

		return self.textctrl.CanCopy()

	def CanCut(self) -> bool:
		"""
		Returns True if the selection can be cut to the clipboard.

		:rtype: bool
		"""

		return self.textctrl.CanCut()

	def CanPaste(self) -> bool:
		"""
		Returns True if the contents of the clipboard can be pasted into the text control.

		On some platforms (Motif, GTK) this is an approximation and returns True if the control is editable, False otherwise.

		:rtype: bool
		"""

		return self.textctrl.CanPaste()

	def CanRedo(self) -> bool:
		"""
		Returns True if there is a redo facility available and the last operation can be redone.

		:rtype: bool
		"""

		return self.textctrl.CanRedo()

	def CanUndo(self) -> bool:
		"""
		Returns True if there is an undo facility available and the last operation can be undone.

		:rtype:	bool
		"""

		return self.textctrl.CanUndo()

	def Clear(self):
		"""
		Clears the text in the control.

		Note that this function will generate a wxEVT_TEXT event, i.e. its effect is identical to calling SetValue (“”).
		"""

		self.textctrl.Clear()

	def Copy(self):
		"""
		Copies the selected text to the clipboard.
		"""

		return self.textctrl.Copy()

	def Cut(self):
		"""
		Copies the selected text to the clipboard and removes it from the control.
		"""

		return self.textctrl.Cut()

	def GetLastPosition(self) -> wx.TextPos:
		"""
		Returns the zero based index of the last position in the text control, which is equal to the number of characters in the control.

		:rtype:	wx.TextPos
		"""

		return self.textctrl.GetLastPosition()

	def GetSelection(self) -> Tuple:
		"""
		Gets the current selection span.

		If the returned values are equal, there was no selection. Please note that the indices returned may be used with the other wx.TextCtrl methods but don’t necessarily represent the correct indices into the string returned by GetValue for multiline controls under Windows (at least,) you should use GetStringSelection to get the selected text.

		:rtype:	tuple
		"""

		return self.textctrl.GetSelection()

	def GetStringSelection(self) -> str:
		"""
		Gets the text currently selected in the control.

		If there is no selection, the returned string is empty.

		:rtype:	string
		"""

		return self.textctrl.GetStringSelection()

	def GetValue(self) -> str:
		"""
		Gets the contents of the control.

		Notice that for a multiline text control, the lines will be separated by (Unix-style) \n characters, even under Windows where they are separated by a \r\n sequence in the native control.

		:rtype:	string
		"""

		return self.textctrl.GetValue()

	def IsEditable(self) -> bool:
		"""
		Returns True if the controls contents may be edited by user (note that it always can be changed by the program).

		In other words, this functions returns True if the control hasn’t been put in read-only mode by a previous call to SetEditable .

		:rtype:	bool
		"""

		return self.textctrl.IsEditable()

	def IsEmpty(self) -> bool:
		"""
		Returns True if the control is currently empty.

		This is the same as GetValue .empty() but can be much more efficient for the multiline controls containing big amounts of text.

		:rtype:	bool
		"""

		return self.textctrl.IsEmpty()

	def Paste(self):
		"""
		Pastes text from the clipboard to the text item.
		"""

		return self.textctrl.Paste()

	def Redo(self):
		"""
		If there is a redo facility and the last operation can be redone, redoes the last operation.

		Does nothing if there is no redo facility.
		"""

		return self.textctrl.Redo()

	def Remove(self, from_: int, to_: int):
		"""
		Removes the text starting at the first given position up to (but not including) the character at the last position.

		This function puts the current insertion point position at to as a side effect.

		:param from_: The first position
		:type from_: long
		:param to_: The last position
		:type to_: long
		"""

		return self.textctrl.Remove(from_, to_)

	def Replace(self, from_: int, to_: int, value) -> str:
		"""
		Replaces the text starting at the first position up to (but not including) the character at the last position with the given text.

		This function puts the current insertion point position at to as a side effect.

		:param from_: The first position
		:type from_: long
		:param to_: The last position
		:type to_: long
		:param value: The value to replace the existing text with
		:type value: string
		"""

		return self.textctrl.Replace(from_, to_, value)

	def SelectAll(self):
		"""
		Selects all text in the control.

		See also SetSelection
		"""

		return self.textctrl.SelectAll()

	def SelectNone(self):
		"""
		Deselects selected text in the control.
		"""

		return self.textctrl.SelectNone()

	def SetSelection(self, from_: int, to_: int):
		"""
		Selects the text starting at the first position up to (but not including) the character at the last position.

		If both parameters are equal to -1 all text in the control is selected.

		Notice that the insertion point will be moved to from by this function.

		:param from_: The first position
		:type from_: long
		:param to_: The last position
		:type to_: long

		See also SelectAll
		"""

		return self.textctrl.SetSelection(from_, to_)

	def SetValue(self, value):
		"""
		Sets the new text control value.

		It also marks the control as not-modified which means that IsModified() would return False immediately after the call to SetValue .

		The insertion point is set to the start of the control (i.e. position 0) by this function unless the control value doesn’t change at all, in which case the insertion point is left at its original position.

		Note that, unlike most other functions changing the controls values, this function generates a wxEVT_TEXT event. To avoid this you can use ChangeValue instead.

		Parameters:	value (string) – The new value to set. It may contain newline characters if the text control is multi-line.
		"""

		return self.textctrl.SetValue(value)

	def Undo(self):
		"""
		If there is an undo facility and the last operation can be undone, undoes the last operation.

		Does nothing if there is no undo facility.
		"""

		return self.textctrl.Undo()

	def WriteText(self, text: str):
		"""
		Writes the text into the text control at the current insertion position.

		:param text: Text to write to the text control
		:type text: string
		"""

		return self.textctrl.WriteText(text)


# end of class TextCtrlWrapper
