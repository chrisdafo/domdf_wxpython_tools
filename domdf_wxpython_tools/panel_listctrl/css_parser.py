#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  css_parser.py
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

# 3rd party
import tinycss
import webcolors
import wx

# this package
from domdf_wxpython_tools.panel_listctrl.constants import text_defaults, sys_colour_lookup


parser = tinycss.make_parser("page3")


def _parse_css(stylesheet):
	print(stylesheet)
	if stylesheet.errors:
		raise ValueError(stylesheet.errors[0])
	print(stylesheet.rules)
	
	styles = {}
	
	# Remove declarations for other platforms and make
	
	for rule in stylesheet.rules:
		styles[rule.selector.as_css()] = {}
		
		for declaration in rule.declarations:
			name = declaration.name
			value = declaration.value.as_css()
			
			if "color" in name:
				value.lstrip("wx.")
				
				if value.startswith("SYS_COLOUR"):
					# wx.SystemColour
					if value in sys_colour_lookup:
						value = wx.SystemSettings.GetColour(sys_colour_lookup[value])
					else:
						raise ValueError(f"""wx.SystemColour 'value' not recognised.
See https://wxpython.org/Phoenix/docs/html/wx.SystemColour.enumeration.html for the list of valid values""")
				
				elif value.startswith("#"):
					# Hex value, pass to wx.Colour directly
					pass
				
				elif value.startswith("rgb("):
					# RGB value, convert to hex
					rgb_triplet = (int(x) for x in value.lstrip("rgb(").rstrip(")").split(","))
					value = webcolors.rgb_to_hex(rgb_triplet)
				
				else:
					# Named colour, convert to hex
					value = webcolors.name_to_hex(value)
			
			if name == "font-family":
				if value == "decorative":
					value = wx.FONTFAMILY_DECORATIVE
				
				elif value == "roman":
					value = wx.FONTFAMILY_ROMAN
				
				elif value == "script":
					value = wx.FONTFAMILY_SCRIPT
				
				elif value == "swiss":
					value = wx.FONTFAMILY_SWISS
				
				elif value == "modern":
					value = wx.FONTFAMILY_MODERN
				
				else:
					value = wx.FONTFAMILY_DEFAULT
			
			elif name == "font-style":
				if value == "slant":
					value = wx.FONTSTYLE_SLANT
				elif value == "italic":
					value = wx.FONTSTYLE_ITALIC
				else:
					value = wx.FONTSTYLE_NORMAL
			
			elif name == "font-weight":
				if value == "light":
					value = wx.FONTWEIGHT_LIGHT
				elif value == "bolt":
					value = wx.FONTWEIGHT_BOLD
				else:
					value = wx.FONTWEIGHT_NORMAL
			
			styles[rule.selector.as_css()][name] = value
	
	# if li p is not styled, use the default values
	if "li p" not in styles:
		styles["li p"] = text_defaults.copy()
	
	# If li p is missing any parameters, add them from the default values
	styles["li p"] = {**text_defaults, **styles["li p"]}
	
	# if li p::selection is not styled, use the values from p
	if "li p::selection" not in styles:
		styles["li p::selection"] = styles["li p"].copy()
	
	# If li p is missing any parameters, add them from p
	styles["li p::selection"] = {**styles["li p"], **styles["li p::selection"]}
	
	# For each li p class, add undefined values from p
	for style in styles:
		if style.split(".")[0] == "li p":
			if style == "li p":
				continue
			if "::selection" in style:
				continue
			styles[style] = {**styles["li p"], **styles[style]}
	
	# For each p::selection class, add undefined values from p::selection
	for style in styles:
		if style.split(".")[0] == "li p":
			if style == "li p::selection":
				continue
			if "::selection" not in style:
				continue
			styles[style] = {**styles["li p::selection"], **styles[style]}
	
	return styles


def parse_css_file(filename):
	stylesheet = parser.parse_stylesheet_file(css_file=filename)
	
	return _parse_css(stylesheet)


def parse_css(css_data):
	stylesheet = parser.parse_stylesheet(css_unicode=css_data)
	
	return _parse_css(stylesheet)

