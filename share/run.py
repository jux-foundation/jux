#!/usr/bin/env python3

#    compile.py
#       Copyright (C) 2011-`date +%Y`  Hamed Saleh and Mahrud Sayrafi
#
#       This program comes with ABSOLUTELY NO WARRANTY.
#       This is free software, and you are welcome to redistribute it
#       under certain conditions; see LICENSE for details.

import os
from log import record, err_log_fd, bin_log_fd
from config import *
from subprocess import Popen as call

def execute(code):
    addr = '%s/%i.%s' % (bin_path, code.subid, ext)
    jailer, jailer_args = jailers[code.lang]

    record('core', pid, '%s starting ...' % (jailer))
    ret = call('%s/%s %s %s' % 
        (judge_path, jailer, addr, ' '.join(jailer_args)), #TODO jailer_args
        stdout = bin_log_fd, stderr = bin_log_fd, shell = True) #FIXME bin_log or jail_log?

    ret.wait(timeout=binary_timeout)

    results=['1','2','3','4'] # FIXME

    record(jailer, ret.pid, 'Returned %i' % (ret.returncode))
    record(jailer, ret.pid, 'Result:\t%s' % (' '.join(results)))

def report():
    print('all')
