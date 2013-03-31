#!/usr/bin/env python3

#    options.py
#       Copyright (C) 2011-`date +%Y`  Hamed Saleh and Mahrud Sayrafi

#       This program comes with ABSOLUTELY NO WARRANTY.
#       This is free software, and you are welcome to redistribute it
#       under certain conditions; see LICENSE for details.

from argparse import ArgumentParser, FileType

parser = ArgumentParser()
parser.add_argument('-i', '--subid',    metavar='ID', type=int, required=True)
parser.add_argument('-u', '--user',     metavar='USER', default='nobody')
parser.add_argument('-p', '--problem',  metavar='PROBLEM', required=True)
parser.add_argument('code',             metavar='CODE', type=FileType('r'))

parser.add_argument('-l', '--lang',     metavar='LANGUAGE', default='cpp')
parser.add_argument('-m', '--mode', choices=['acm','ioi'], default='ioi')
#args = parser.parse_args('-i 12 -u mahrud -p hellow code.cpp'.split())
args = parser.parse_args()
