#!/usr/bin/python3

#    log.py
#    Copyright (C) 2011-`date +%Y`  Hamed Saleh and Mahrud Sayrafi
#
#    This program comes with ABSOLUTELY NO WARRANTY.
#    This is free software, and you are welcome to redistribute it
#    under certain conditions; see LICENSE for details.

# http://docs.python.org/3.3/library/logging.html

from os import getppid
from sys import stderr
import config
import datetime

def record(process, pid, msg, parent='jux', ppid=getppid()):
    timestamp = datetime.datetime.now().strftime(config.timestamp_format)
    print('%s    %s    %s[%i]:    %s' % 
        (timestamp, config.hostname, process, pid, msg), file=stderr)
#    print( '%s    %s    %s[%i]:    %s' % 
#        (timestamp, config.hostname, process, pid, msg), file=config.errlog)
