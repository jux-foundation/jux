#!/usr/bin/env python3

#    core.py
#       Copyright (C) 2011-`date +%Y`  Hamed Saleh and Mahrud Sayrafi

#       This program comes with ABSOLUTELY NO WARRANTY.
#       This is free software, and you are welcome to redistribute it
#       under certain conditions; see LICENSE for details.

from config import *
from log import record
from os import getpid, getppid
import os
from compile import compile
#import run
#import output

pid = getpid()
ppid = getppid()

record('core', pid, 'Core started: (ppid: %i)' % (ppid))
record('core', pid, '%i:%s:%s:%s:%s' % 
    (args.subid, args.user, args.problem, args.code.name, args.lang))

compile(args.subid, os.path.abspath(args.code.name), args.lang)

#run()

#return

