#!/bin/sh

JUX_PREFIX=/judge
LOCK=$JUX_PREFIX/run/jux/jux.pid	#FIXME

if [ -e $LOCK ]
then
	PID=`cat $LOCK`

	if ps $PID >/dev/null
	then
		echo "Daemon is already running and it's PID is $PID." >&2
		exit 1
	else
		rm -f $LOCK
	fi
fi

sh $JUX_PREFIX/base/daemon.sh &>> $JUX_PREFIX/var/log/jux/error.log &
#cp /var/www/html/hellicode.php- /var/www/html/hellicode.php
