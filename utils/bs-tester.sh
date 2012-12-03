#!/bin/sh
#
#   tester.sh - tests whether or not the judge is working properly without web
#   Copyright (C) 2012  Hamed Saleh and Mahrud Sayrafi

#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.

#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.

#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.

echo -1 \
	admin \
	bs \
	cpp \
	/judge/problems/bs/bs.cpp \
	0 | #FIXME: what was this?! guess smt like whether or not break on wrong
	nc -vv 127.0.0.1 31416

sleep 2 # Ladies and gentlemen, please wait for the jury to make its decision!

tail -n3 /judge/var/log/jux/error.log # in case there are some errors, they are here!
tail -n1 /judge/var/log/jux/grading.log # and there you go! the final decision!
