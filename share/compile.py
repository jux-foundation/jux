#!/usr/bin/env python3

#    compile.py
#       Copyright (C) 2011-`date +%Y`  Hamed Saleh and Mahrud Sayrafi
#
#       This program comes with ABSOLUTELY NO WARRANTY.
#       This is free software, and you are welcome to redistribute it
#       under certain conditions; see LICENSE for details.

import config
from config import pid, compilers
from os import system
from log import record

def compile(subid, code, lang):
    addr = '%s/%i.%s' % (config.source_path, subid, lang)
    system('cp -f %s %s' % (code, addr))

    code = addr
    compiler, compiler_args = compilers[lang]

    record('core', pid, '%s starting ...' % (compiler))

    ret = system('%s %s %s' % (compiler, code, ' '.join(compiler_args)))

    cpid = -1 # FIXME: this is supposed to be the compiler's pid

    record(compiler, cpid, 'Returned %i' % (ret))
    #TODO: record compiler warnings/errors to file
