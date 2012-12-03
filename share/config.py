#!/usr/bin/env python3

#	config.py
#       Copyright (C) 2011-`date +%Y`  Hamed Saleh and Mahrud Sayrafi
#
#       This program comes with ABSOLUTELY NO WARRANTY.
#       This is free software, and you are welcome to redistribute it
#       under certain conditions; see LICENSE for details.

import sys

sys.path.append ('/etc/jux')

import core_config
keys = vars (core_config)
conf = type ("Conf", 

for key in keys:
	print key, keys[key]
