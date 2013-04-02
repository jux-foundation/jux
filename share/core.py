#!/usr/bin/env python3

#    core.py
#       Copyright (C) 2011-`date +%Y`  Hamed Saleh and Mahrud Sayrafi

#       This program comes with ABSOLUTELY NO WARRANTY.
#       This is free software, and you are welcome to redistribute it
#       under certain conditions; see LICENSE for details.

from config import *
from options import code
from log import record

from compile import compile
from run import execute
#import output

record('core', pid, 'Core started: (ppid: %i)' % (ppid))
record('core', pid, '%i:%s:%s:%s:%s' % 
    (code.subid, code.owner, code.prob, code.addr.name, code.lang))

compile(code)

execute(code)

#return

