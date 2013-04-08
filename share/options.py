#!/usr/bin/env python3

#    options.py
#       Copyright (C) 2011-`date +%Y`  Hamed Saleh and Mahrud Sayrafi

#       This program comes with ABSOLUTELY NO WARRANTY.
#       This is free software, and you are welcome to redistribute it
#       under certain conditions; see LICENSE for details.

import os
import config
import textwrap
from argparse import ArgumentParser, FileType, HelpFormatter, SUPPRESS

parser = ArgumentParser(prog = 'core', 
    description = 'Jux: the secure judge for Linux', 
    formatter_class=lambda prog: 
        HelpFormatter(prog, max_help_position = 26, width=79))

#FIXME: use http://docs.python.org/2/library/argparse.html#mutual-exclusion

parser.add_argument('-i', '--subid', dest='subid', type=int, required=True, 
    help = 'the unique ID for each code', metavar='ID')

parser.add_argument('-o', '--owner', dest='owner', default=os.getlogin(), 
    help = 'the owner of the code (default: shell owner)', 
    metavar = 'USER')

parser.add_argument('-p', '--prob',  dest='prob', required=True, 
    help = 'the targeted problem')

parser.add_argument('addr',          type=FileType('r'), 
    help = 'the code to be judges')


parser.add_argument('-l', '--lang',  dest='lang', 
    help = '''language of the code; if not provided, use the ext.''')

parser.add_argument('-m', '--mode',  dest='mode', 
    choices=['acm','ioi'], default='ioi', 
    help = '''contest mode; options:\n\t
        acm: stop at first wrong test;\n\t
        ioi: test 'em all (default)''')


parser.add_argument('-t', '--tests', dest='tests', nargs='+',
    help = 'a list of testcases to be used')

parser.add_argument('--custom-test', dest='ctest', type=FileType('r'),
    help = 'a custom test to be given to the program')


parser.add_argument('--skip-compile', dest='compiled', action='store_true',
    help = 'don\'t compile again if binary exists (see --rejudge)')

parser.add_argument('-r', '--rejudge', dest='rejudge', action='store_true',
    help = 'rejudge the code (compiles again; see --skip-compile)')


parser.add_argument('--error-log',   dest='err_log', type=FileType('w'),
    help = SUPPRESS)

parser.add_argument('--compile-log', dest='comp_log', type=FileType('w'),
    help = SUPPRESS)

parser.add_argument('--binary-log', dest='bin_log', type=FileType('w'),
    help = SUPPRESS)

parser.add_argument('--log-path', dest='log_path', type=FileType('w'),
    help = SUPPRESS)


args = parser.parse_args('-i 12 -o mahrud -p hellow code.cpp'.split())
#args = parser.parse_args()


if args.log_path:
    log_path = args.log_path
if args.err_log:
    err_log = args.err_log
if args.comp_log:
    comp_log = args.comp_log
if args.bin_log:
    bin_log = args.bin_log

if args.tests:
    tests = args.tests
elif args.ctest:
    tests = [-1]
    ctest_addr = args.ctest
else:
    print('FIXME')
#    tests = range(config.problem_conf[args.prob]['tests'])

if not args.lang:
    args.lang = args.addr.name.split('.')[-1]

if args.rejudge:
    print('FIXME')
if args.compiled:
    print('FIXME')

code = config.submission(args)
