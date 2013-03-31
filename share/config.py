#!/usr/bin/env python3

#    config.py
#       Copyright (C) 2011-`date +%Y`  Hamed Saleh and Mahrud Sayrafi
#
#       This program comes with ABSOLUTELY NO WARRANTY.
#       This is free software, and you are welcome to redistribute it
#       under certain conditions; see LICENSE for details.

from os import getpid
import sys
from socket import gethostname
from options import args

sys.path[0:0] = ['/judge/etc/jux']
from juxd_config import *

pid = getpid()
hostname = gethostname()
jail_path = '/mnt/jail'
bin_path = jail_path + '/home'
source_path = jail_path + '/source'
compilers = {'cpp': ['g++', ['-o %s/%i.out' % (bin_path, args.subid)]]}
