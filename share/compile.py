#!/usr/bin/env python3

#    compile.py
#       Copyright (C) 2011-`date +%Y`  Hamed Saleh and Mahrud Sayrafi
#
#       This program comes with ABSOLUTELY NO WARRANTY.
#       This is free software, and you are welcome to redistribute it
#       under certain conditions; see LICENSE for details.

import os
from log import record, err_log_fd, comp_log_fd
from config import *
from subprocess import Popen as call

def compile(code):
    addr = '%s/%i.%s' % (src_path, code.subid, code.lang)
    call('cp -f %s %s' % (os.path.abspath(code.addr.name), addr), 
        stderr = err_log_fd, shell = True)

    compiler, compiler_args = compilers[code.lang]

    record('core', pid, '%s starting ...' % (compiler))
    ret = call('%s %s %s' % 
        (compiler, addr, ' '.join(compiler_args) % (code.subid)), 
        stdout = comp_log_fd, stderr = comp_log_fd, shell = True)

    ret.wait(timeout = compile_timeout)

    record(compiler, ret.pid, 'Returned %i' % (ret.returncode))
