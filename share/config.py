#!/usr/bin/env python3

#    config.py
#       Copyright (C) 2011-`date +%Y`  Hamed Saleh and Mahrud Sayrafi
#
#       This program comes with ABSOLUTELY NO WARRANTY.
#       This is free software, and you are welcome to redistribute it
#       under certain conditions; see LICENSE for details.

import sys
from os import getpid, getppid, getlogin
from socket import gethostname

sys.path[0:0] = ['/judge/etc/jux']
from juxd_config import *

pid = getpid()
ppid = getppid()
owner = getlogin()
hostname = gethostname()

#FIXME move everything below here until the submission class to juxd_config

judge_path = '/judge/share'

jail_path = '/mnt/jail'
bin_path = jail_path + '/home'
src_path = jail_path + '/source'
log_path = jail_path + '/var/log' #FIXME
err_log = 'error.log'
comp_log = None
bin_log = None

timestamp_format="%b %d %H:%M:%S.%f"

ext = 'out' #FIXME, depending on lang?

compilers = {'cpp': ['g++', ['-o %s/%%i.%s' % (bin_path, ext)]],
             'c':   ['gcc', ['-o %s/%%i.%s' % (bin_path, ext)]]}
# the compilers[lang][1][0] must be the output argument and it must 
# have "%%i" in it, because the output must have the subid.

jail_uid = 99
jail_gid = 99

jailers = {'cpp': ['jail.sh', ['%s %i:%i' % (jail_path, jail_uid, jail_gid)]],   #FIXME
           'c':   ['jail.sh', ['%s %i:%i' % (jail_path, jail_uid, jail_gid)]]}

compile_timeout = 5
binary_timeout = 5

class submission:
    def __init__(self, data):
        self.subid = data.subid
        self.owner = data.owner
        self.prob = data.prob
        self.addr = data.addr
        self.lang = data.lang

    def compile(self):  #TODO: hmmm, what?
        compile.compile(self)

from options import *

