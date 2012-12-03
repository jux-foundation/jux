#!/bin/sh

#	compile.sh
#	Copyright (C) 2011-`date +%Y`  Hamed Saleh and Mahrud Sayrafi

#	This program comes with ABSOLUTELY NO WARRANTY.
#	This is free software, and you are welcome to redistribute it
#       under certain conditions; see LICENSE for details.

$TIMEOUT $COMPILE_TIME \
	$CHROOT --userspec=$BIN_USER:$BIN_GROUP $JAIL \
	$COMPILER_DIR/$LANGUAGE.sh 

exit $?
