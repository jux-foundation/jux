#!/bin/sh

#	jail.sh
#       Copyright (C) 2011-`date +%Y`  Hamed Saleh and Mahrud Sayrafi

#       This program comes with ABSOLUTELY NO WARRANTY.
#       This is free software, and you are welcome to redistribute it
#       under certain conditions; see LICENSE for details.

echo $@
exit

TEST=$1 shift
TIME_LIMIT=`expr 2 \* $1` shift
FIRST_INPUT=$@

FIFORUN="/tmp/fiforun$$"

{
	mkfifo $FIFORUN
#	exec 3<>$FIFORUN

	sh -c "$FIRST_INPUT" >$FIFORUN &
	sleep 0.1
	coproc $TESTER $INIT_DIR/$TEST.init >$FIFORUN &

	exec <$FIFORUN >&${COPROC[1]}	\
		$TIME -f "result $TIME_FORMAT"	\
		$TIMEOUT --signal=SIGKILL $TIME_LIMIT	\
		$SU $RUN_USER \
		$SU_SYNTAX $OUT
#		$SU_SYNTAX "$OUT 2>/dev/null"				# FIXME
}  2>&1

rm -f $FIFORUN
