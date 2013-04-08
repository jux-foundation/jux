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
from config import code, timestamp_format, hostname
from config import log_path, err_log, comp_log, bin_log
import datetime

err_log_fd = open('%s/%s' % 
    (log_path, err_log), 'a')

comp_log_fd = open('%s/%i-%s-%s-%s.log' % 
    (log_path, code.subid, code.owner, code.prob, code.lang), 'w')

bin_log_fd = open('%s/%i-%s-%s-%s.log' % 
    (log_path, code.subid, code.owner, code.prob, 'bin'), 'w') # TODO 'w+b'?


def record(process, pid, msg, parent = 'jux', ppid=getppid()):
    timestamp = datetime.datetime.now().strftime(timestamp_format)
    print("%s\t%s\t%s[%i]:\t%s" % 
        (timestamp, hostname, process, pid, msg), file = stderr)
    print("%s\t%s\t%s[%i]:\t%s" % 
        (timestamp, hostname, process, pid, msg), file = err_log_fd)
