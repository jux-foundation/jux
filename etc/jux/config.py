#!/usr/bin/python3

#	This is the main Jux daemon configuration file.  It contains the
#	configuration directives and customizations.
#	See <URL:http://hellicode.allamehelli.ir/> for detailed information.

#	General configurations:

#ServerRoot=
#PidFile=
#User
#Group
#ServerAdmin

#	Forking configurations?			# FIXME

#MaxRequests=
#Timeout=

#StartServers
#MaxSpareServers
#MaxClients
#MaxRequestsPerChild

#	Network configurations:

#Listen # 31415, *:31415, 127.0.0.1:31415, 192.168.1.0/24:31415, [::1]:31415

#	Modules:

#LoadModule # ...

#	Custom config files:

#Include # ...

#	Compiler configurations:

#COMPILER_DIR="/bin/compilers"
#COMPILE_TIME=10                  # FIXME
#BIN_USER=0
#BIN_GROUP=0
#COMPILER="$BASE/compile.sh"

#	Jail & Jailer configurations:

#JAILER="$BASE/jail.sh"
#JAIL="$JUDGE/jail"
#SU_SYNTAX="--session-command"
#CODE_DIR='/source'				# FIXME
#RUN_DIR='/home'                  # FIXME
#RUN_USER='judge'					# FIXME
#RUN_GROUP=99
#compile uid
#jail uid

#	Problem configurations:

#PROBLEMS_DIR="$JUDGE/problems"

#	Logging configurations:

#LOG_DIR="$JUDGE/var/log/jux"
#LOG_DATE_FORMAT="--rfc-3339=ns"

#TIME_FORMAT='%e %M %x'

#ErrorLog
#LogLevel
#LogFormat

#	Security and cryptography:

#ServerSignature


#	Mysql configurations:

DB_HOST='127.0.0.1'
DB_USERNAME=''
DB_PASSWORD=''
DB_NAME=''

# Templates:

#for Modules:

#<IfModule mod_disk_cache.c>
#   CacheEnable disk /
#   CacheRoot "/var/cache/mod_proxy"
#</IfModule>

#For zombies or different contest interfaces:

#<VirtualHost *:80>
#    ServerAdmin webmaster@dummy-host.example.com
#    DocumentRoot /www/docs/dummy-host.example.com
#    ServerName dummy-host.example.com
#    ErrorLog logs/dummy-host.example.com-error_log
#    CustomLog logs/dummy-host.example.com-access_log common
#</VirtualHost>
