#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  panel_listctrl.py
"""
A custom Panel that acts as a ListCtrl for other wx.Panel objects.

An example ListItem exists that provides two StaticText fields and
can be used as the basis for custom list items
"""
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
# generated by wxGlade 0.9.2 on Thu Jan 16 16:34:51 2020
#

# stdlib
import pathlib

# 3rd party
import wx

# this package
from domdf_wxpython_tools.panel_listctrl.css_parser import parse_css, parse_css_file
from domdf_wxpython_tools.panel_listctrl.font_parser import parse_font


# begin wxGlade: dependencies
# end wxGlade

# begin wxGlade: extracode
# end wxGlade


class PanelListCtrl(wx.ScrolledWindow):
	def __init__(
			self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.DefaultSize,
			style=wx.TAB_TRAVERSAL, name=wx.PanelNameStr, left_padding=32):
			
		wx.ScrolledWindow.__init__(self, parent, id, pos=pos, size=size, style=style | wx.TAB_TRAVERSAL, name=name)

		self._items = []
		self.parent = parent
		self.left_padding = left_padding

		self.SetScrollRate(10, 10)
		
		self.sizer_1 = wx.BoxSizer(wx.VERTICAL)
		self.SetSizer(self.sizer_1)
		self.sizer_1.Fit(self)
		
		self.Layout()
		
		self.Bind(wx.EVT_LIST_ITEM_SELECTED, self._on_selection_changed)
		self.Bind(wx.EVT_LIST_KEY_DOWN, self._on_key_down)
		
		self.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_LISTBOX))
		
	def _on_selection_changed(self, event):
		"""
		Handler for EVT_LIST_ITEM_SELECTED, triggered by clicking on an Item
		"""
		
		for item in self._items:
			if item == event.GetEventObject():
				item.SelectItem()
			else:
				item.DeselectItem()
		
		event.Skip()

	def _on_key_down(self, event):
		"""
		Handler for EVT_LIST_KEY_DOWN, triggered by pressing key on keyboard when an item is focused
		"""
		
		key_code = event.GetKeyCode()
		index = self.GetItemPosition(event.GetEventObject())

		self.DeselectAll()
		
		if key_code == wx.WXK_UP:
			index = index - 1
		elif key_code == wx.WXK_DOWN:
			index = index + 1
		
		if key_code == wx.WXK_PAGEUP:
			index = index - 5
		elif key_code == wx.WXK_PAGEDOWN:
			index = index + 5
		
		if index >= self.GetItemCount():
			index = self.GetItemCount()-1
		elif index < 0:
			index = 0
		
		self.Select(index)
		
		event.Skip()
		# TODO: Keyboard autocompletion?

	def SetSelection(self, idx):
		"""
		Set the current selection to the item at the given index
		
		:param idx: index of the item to select
		:type idx: int
		"""
		
		item_to_select = self.GetItem(idx)
		
		for item in self._items:
			if item == item_to_select:
				item.SelectItem()
			else:
				item.DeselectItem()
	
	def DeselectAll(self):
		"""
		Deselect all items
		"""
		
		for i in range(self.GetItemCount()):
			self.Select(i, False)
	
	def AcceptsFocus(self):
		return True
	
	def AcceptsFocusFromKeyboard(self):
		return False
	
	def Append(self, panel_list_item):
		"""
		Append a 'PanelListItem' object, or an instance of a custom subclass, to the control.
		"""
		
		self.sizer_1.Add(panel_list_item, 0, wx.EXPAND, wx.TOP, 0)
		self._items.append(panel_list_item)
		self.sizer_1.Fit(self)
		self.Layout()

	def AppendNewItem(self, text_dict, style_data):
		"""
		Append a new 'PanelListItem' object to the control, passing the 'text_dict' and 'style_data'
		parameters to the new object.
		
		:param text_dict:
		:type text_dict:
		:param style_data:
		:type style_data:
		
		:return: The new PanelListItem object that was added to the control
		:rtype:
		"""
		
		item = PanelListItem(self, text_dict, style_data, left_padding=self.left_padding)
		self.Append(item)
		return item
		
	def Clear(self):
		"""
		Removes all items from the control
		"""
		
		for item in self._items:
			self.sizer_1.Hide(item)
			self.sizer_1.Remove(0)
			
			item.Destroy()
			self.Layout()
		
		self._items = []
		
		event = wx.ListEvent(wx.wxEVT_LIST_DELETE_ALL_ITEMS)
		event.SetEventObject(self)
		wx.PostEvent(self, event)
		
		return True
	
	def DeleteItem(self, item):
		"""
		Deletes the specified item from the control.
		
		:param item:
		:type item:
		
		:return: True if the item was removed, False otherwise (usually because the item wasn't in the control)
		:rtype: bool
		"""
		
		for index, widget in enumerate(self._items):
			if widget == item:
				self.sizer_1.Hide(self._items.pop(index))
				self.sizer_1.Remove(index)
				
				item.Destroy()
				
				self.Layout()
				
				event = wx.ListEvent(wx.wxEVT_LIST_DELETE_ITEM)
				event.SetEventObject(self)
				wx.PostEvent(self, event)
				
				return True
		
		return False

	def Focus(self, idx):
		""" Set Focus to the the given item. """
		for index, item in enumerate(self._items):
			if index == idx:
				item.SelectItem()
			else:
				item.DeselectItem()

	def GetColumnCount(self):
		"""
		Returns the number of columns.
		"""
		
		return 1

#
# 	def GetCountPerPage(self):
# 		"""
# 		GetCountPerPage() -> int
#
# 		Gets the number of items that can fit vertically in the visible area
# 		of the list control (list or report view) or the total number of items
# 		in the list control (icon or small icon view).
# 		"""
# 		return 0
#
	
	def GetFirstSelected(self, *args):
		"""
		Returns the first selected item, or -1 when none is selected.
		
		:param args:
		:type args:
		
		:return:
		:rtype:
		"""
		
		for item in self._items:
			if item.IsSelected():
				return item
		
		return -1

	def GetFocusedItem(self):
		"""
		Gets the currently focused item or -1 if none is focused.
		
		:return:
		:rtype:
		"""
		
		for item in self._items:
			if item.IsSelected():
				return item
		
		return -1

	def GetItem(self, itemIdx, *args):
		"""
		GetItem(itemIdx, col=0) -> ListItem

		Gets information about the item. See SetItem() for more information.
		
		:param itemIdx:
		:type itemIdx:
		:param args:
		:type args:
		
		:return:
		:rtype:
		"""
		
		return self._items[itemIdx]
		
	def GetItemBackgroundColour(self, item):
		"""
		GetItemBackgroundColour(item) -> Colour

		Returns the colour for this item.
		"""
		
		return item.GetBackgroundColour()

	def GetItemCount(self):
		"""
		Returns the number of items in the list control.
		
		:return:
		:rtype:
		"""
		
		return len(self._items)

	def GetItemPosition(self, item):
		"""
		GetItemPosition(item) -> Point

		Returns the position of the item, or -1 if it is not found
		"""
		if item in self._items:
			return self._items.index(item)
		
		return -1

	def GetNextSelected(self, item):
		"""
		Returns subsequent selected items, or -1 when no more are selected.
		
		:param item:
		:type item:
		
		:return:
		:rtype:
		"""
		
		index_of_item = self.GetItemPosition(item)
		
		for index, item in enumerate(self._items):
			if index <= index_of_item:
				continue
			if item.IsSelected():
				return item
		
		return -1

	def GetSelectedItemCount(self):
		"""
		GetSelectedItemCount() -> int

		Returns the number of selected items in the list control.
		"""
		selected_item_count = 0
		
		for item in self._items:
			if item.IsSelected():
				selected_item_count += 1
		
		return selected_item_count
#
# 	def HitTest(self, point):
# 		"""
# 		HitTest(point) -> (long, flags)
#
# 		Determines which item (if any) is at the specified point, giving
# 		details in flags.
# 		"""
# 		pass
#
# 	def InsertItem(self, *__args): with multiple overloads
# 		"""
# 		InsertItem(info) -> long
# 		InsertItem(index, label) -> long
# 		InsertItem(index, imageIndex) -> long
# 		InsertItem(index, label, imageIndex) -> long
#
# 		Inserts an item, returning the index of the new item if successful, -1
# 		otherwise.
# 		"""
# 		return 0
		# TODO: Trigger EVT_LIST_INSERT_ITEM
#
	def IsEmpty(self):
		"""
		Returns true if the control doesn't currently contain any items.
		
		:return:
		:rtype:
		"""
		
		return bool(self._items)

	def IsSelected(self, idx):
		"""
		Returns ``True`` if the item is selected.
		
		:param idx:
		:type idx:
		
		:return:
		:rtype:
		"""
		
		return self._items[idx].IsSelected()

	def RefreshItem(self, item):
		"""
		Redraws the given item.
		
		:param item:
		:type item:
		
		:return:
		:rtype:
		"""
		
		item.Layout()
		item.Refresh()

	def RefreshItems(self, itemFrom, itemTo):
		"""
		Redraws the items between itemFrom and itemTo.
		
		:param itemFrom:
		:type itemFrom:
		:param itemTo:
		:type itemTo:
		
		:return:
		:rtype:
		"""
		
		for index in range(itemFrom, itemTo+1):
			self.RefreshItem(self._items[index])
#
# 	def ScrollList(self, dx, dy):
# 		"""
# 		ScrollList(dx, dy) -> bool
#
# 		Scrolls the list control.
# 		"""
# 		return False

	def Select(self, idx, on=1):
		"""
		Selects/deselects an item.
		
		:param idx:
		:type idx:
		:param on:
		:type on:
		
		:return:
		:rtype:
		"""
		
		self._items[idx].SelectItem(on)

# 	def SortItems(self, fnSortCallBack):
# 		"""
# 		SortItems(fnSortCallBack) -> bool
#
# 		Call this function to sort the items in the list control.
# 		"""
# 		return False
#
	@property
	def ColumnCount(self):
		"""
		Returns the number of columns.
		
		:rtype: int
		"""
		return 1

#
# 	CountPerPage = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
# 	"""GetCountPerPage() -> int
#
# Gets the number of items that can fit vertically in the visible area
# of the list control (list or report view) or the total number of items
# in the list control (icon or small icon view)."""
#
#
	@property
	def FocusedItem(self):
		"""
		Gets the currently focused item or -1 if none is focused.
		
		:return:
		:rtype:
		"""
		
		return self.GetFocusedItem()

	
	@property
	def ItemCount(self):
		"""
		Returns the number of items in the list control.
		
		:rtype: int
		"""
		return len(self._items)

# end of class RecentProjectsPanel


class PanelListItem(wx.Panel):
	def __init__(
			self, parent, text_dict, style_data, id=wx.ID_ANY,
			style=0, name=wx.PanelNameStr, left_padding=32
			):
		"""
		
		:param parent: The PanelListCtrl the item is to go into
		:type parent: PanelListCtrl
		:param text_dict:
		:type text_dict:
		:param style_data:
		:type style_data:
		:param id: An identifier for the panel. ID_ANY is taken to mean a default.
		:type id: wx.WindowID
		:param style: The window style. See wx.Panel.
		:type style: int
		:param name: Window name
		:type name: str
		:param left_padding: the spacing to the left of the text in the control
		:type left_padding: int
		"""
		
		self.parent = parent
		
		if not isinstance(text_dict, dict):
			raise TypeError("'text_dict' must be a dict containing 'css class:text' pairs")
		
		if isinstance(style_data, pathlib.Path):
			# Filename provided
			style_data = parse_css_file(style_data)
		if isinstance(style_data, str):
			# Filename or css provided
			try:
				# CSS
				style_data = parse_css(style_data)
			except ValueError:
				# Filename
				style_data = parse_css_file(style_data)
		
		elif not isinstance(style_data, dict):
			raise TypeError("""'style_data' must be either:
	> A string or pathlib.Path object pointing to a css file, or
	> A dictionary containing the style data, or
	> A string containing css properties.""")
		
		self.style_data = style_data
		
		wx.Panel.__init__(self, parent, id, style=style | wx.TAB_TRAVERSAL | wx.WANTS_CHARS, name=name)
		
		self.selected = False
		
		# Bind events
		self.Bind(wx.EVT_LEFT_UP, self.OnClick)
		self.Bind(wx.EVT_LEFT_DCLICK, self.OnDoubleClick)
		self.Bind(wx.EVT_MIDDLE_UP, self.OnMiddleClick)
		self.Bind(wx.EVT_KEY_DOWN, self.OnKeyDown)

		# for wxMSW
		self.Bind(wx.EVT_COMMAND_RIGHT_CLICK, self.OnRightClick)
		
		# for wxGTK
		self.Bind(wx.EVT_RIGHT_UP, self.OnRightClick)
		
		# Background colour settings for panel
		if "li" in self.style_data and "background-color" in self.style_data["li"]:
			self._default_background = self.style_data["li"]["background-color"]
		else:
			self._default_background = wx.SystemSettings.GetColour(wx.SYS_COLOUR_LISTBOX)
		
		if "li::selection" in self.style_data and "background-color" in self.style_data["li::selection"]:
			self._selected_background = self.style_data["li::selection"]["background-color"]
		else:
			self._selected_background = wx.SystemSettings.GetColour(wx.SYS_COLOUR_MENUHILIGHT)
		
		self._items = {}
		self._text_properties = {}
		
		self.outer_sizer = wx.BoxSizer(wx.HORIZONTAL)
		main_grid = wx.FlexGridSizer(len(text_dict), 2, 0, left_padding)
		
		for index, (css_class, text) in enumerate(text_dict.items()):
			widget = wx.StaticText(self, wx.ID_ANY, text, style=wx.ST_ELLIPSIZE_MIDDLE)
			self._items[css_class] = widget
			
			if index == 0:
				main_grid.Add((0, 0), 0, 0, 0)
				main_grid.Add(widget, 0, wx.TOP, 6)
			else:
				main_grid.Add((0, 0), 0, 0, 0)
				main_grid.Add(widget, 0, wx.TOP, 0 if wx.Platform == "__WXGTK__" else 2)
			
			widget.Bind(wx.EVT_LEFT_UP, self.OnClick)
			widget.Bind(wx.EVT_KEY_DOWN, self.OnKeyDown)
			widget.Bind(wx.EVT_LEFT_DCLICK, self.OnDoubleClick)
			widget.Bind(wx.EVT_MIDDLE_UP, self.OnMiddleClick)
			# for wxMSW
			widget.Bind(wx.EVT_COMMAND_RIGHT_CLICK, self.OnRightClick)
			
			# for wxGTK
			widget.Bind(wx.EVT_RIGHT_UP, self.OnRightClick)
		
		self.outer_sizer.Add(main_grid, 0, wx.BOTTOM, 4)
		
		self.SetSizer(self.outer_sizer)
		self.outer_sizer.Fit(self)
		self.Layout()
		
		self.Refresh()
	
	def SelectItem(self, select=True):
		self.selected = select
		if select:
			self.SetFocus()
		self.Refresh()
	
	def DeselectItem(self):
		self.selected = False
		self.Refresh()
		event = wx.ListEvent(wx.wxEVT_LIST_ITEM_DESELECTED)
		event.SetEventObject(self)
		wx.PostEvent(self, event)
	
	def OnRightClick(self, event):
		event = wx.ListEvent(wx.wxEVT_LIST_ITEM_RIGHT_CLICK)
		event.SetEventObject(self)
		wx.PostEvent(self, event)
	
	def OnMiddleClick(self, event):
		event = wx.ListEvent(wx.wxEVT_LIST_ITEM_RIGHT_CLICK)
		event.SetEventObject(self)
		wx.PostEvent(self, event)
	
	def OnClick(self, event):
		event = wx.ListEvent(wx.wxEVT_LIST_ITEM_SELECTED)
		event.SetEventObject(self)
		wx.PostEvent(self, event)
		
	def OnDoubleClick(self, event):
		event = wx.ListEvent(wx.wxEVT_LIST_ITEM_ACTIVATED)
		event.SetEventObject(self)
		wx.PostEvent(self, event)

	def OnKeyDown(self, event):
		key_event = event
		event = wx.ListEvent(wx.wxEVT_LIST_KEY_DOWN)
		event.SetEventObject(self)
		event.SetKeyCode(key_event.GetKeyCode())
		wx.PostEvent(self, event)
	
	def IsSelected(self):
		return self.selected
	
	def _refresh_background_colour(self):
		if self.selected:
			wx.Panel.SetBackgroundColour(self, self._selected_background)
		else:
			wx.Panel.SetBackgroundColour(self, self._default_background)
	
	def _refresh_text(self):
		for classname, widget in self._items.items():
			if self.selected:
				class_style_data = self.style_data[f"li p.{classname}::selection"]
			else:
				class_style_data = self.style_data[f"li p.{classname}"]
				
			colour, font_data = parse_font(class_style_data)
			
			widget.SetForegroundColour(colour)
			widget.SetFont(wx.Font(**font_data))
	
	def SetBackgroundColour(self, colour):
		self._default_background = colour
	
	def SetSelectedBackgroundColour(self, colour):
		self._selected_background = colour
	
	def GetBackgroundColour(self):
		return self._default_background
	
	def GetCurrentBackgroundColour(self):
		return wx.Panel.GetBackgroundColour(self)
	
	def Refresh(self, **kwargs):
		self._refresh_background_colour()
		self._refresh_text()
		wx.Panel.Refresh(self)
	
	def GetContents(self):
		return self._items.values()

# end of class RecentProjectItem