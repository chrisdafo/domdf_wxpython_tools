#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  font_parser.py
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
import re
from functools import lru_cache, wraps

# 3rd party
from frozendict import frozendict


def freezeargs(func):
	"""Make mutable dictionary immutable for lru_cache

	From stackoverflow.com/a/53394430
	"""
	
	@wraps(func)
	def wrapped(*args, **kwargs):
		args = tuple(
				[frozendict(arg) if isinstance(arg, dict) else arg for arg in args])
		kwargs = {k: frozendict(v) if isinstance(v, dict) else v for k, v in kwargs.items()}
		return func(*args, **kwargs)
	
	return wrapped


@freezeargs
@lru_cache(5)
def parse_font(style_dict):
	colour = style_dict["color"]
	
	font_data = {
			"family": style_dict["font-family"],
			"style": style_dict["font-style"],
			"weight": style_dict["font-weight"],
			"faceName": style_dict["font-face-name"]
			}
	
	if style_dict["text-decoration"].lower() == "underline":
		font_data["underline"] = True
	
	# if style_dict["font-size"] is None:
	# 	font_data["pointSize"] = None
	# else:
	font_size_value, pt_or_px = filter(None, re.split("(\d+|\D+)", style_dict["font-size"]))

	if pt_or_px.lower() == "pt":
		font_data["pointSize"] = int(font_size_value)
	elif pt_or_px.lower() == "px":
		font_data["pixelSize"] = int(font_size_value)

	return colour, font_data
