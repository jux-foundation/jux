#!/usr/bin/env python3

#    compile.py
#       Copyright (C) 2011-`date +%Y`  Hamed Saleh and Mahrud Sayrafi
#
#       This program comes with ABSOLUTELY NO WARRANTY.
#       This is free software, and you are welcome to redistribute it
#       under certain conditions; see LICENSE for details.

import os
from log import record
from config import *
from subprocess import Popen as call

def execute(code):
    addr = '%s/%i.%s' % (bin_path, code.subid, ext)
    jailer, jailer_args = jailers[code.lang]
    binary_log = open('%s/%i-%s-%s-%s.log' % 
        (log_path, code.subid, code.owner, code.prob, 'binary'), 'w') # TODO 'w+b'?

    record('core', pid, '%s starting ...' % (jailer))
    ret = call('%s/%s %s %s' % 
        (judge_path, jailer, addr, ' '.join(jailer_args)), #TODO jailer_args
        stdout = binary_log, stderr = binary_log, shell = True) #FIXME

    ret.wait(timeout=binary_timeout) # FIXME: why does it return 127?

    results=['1','2','3','4'] # FIXME

    record(jailer, ret.pid, 'Returned %i' % (ret.returncode))
    record(jailer, ret.pid, 'Result:\t%s' % (' '.join(results)))

def report():
    print('all')
