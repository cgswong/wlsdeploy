#!/bin/sh
######################################################
# NAME: startManagedServers.sh
#
# DESC: Starts Managed Server for Oracle WebLogic Server (WLS) domain.
#
# $HeadURL: $
# $LastChangedBy: cgwong $
# $LastChangedDate: $
# $LastChangedRevision: $
#
# LOG:
# yyyy/mm/dd [user] - [notes]
# 2014/01/20 cgwong - [v1.0.0] Creation.
# 2014/01/21 cgwong - [v1.0.1] Updated environments file name.
# 2014/03/19 cgwong - [v1.0.2] Switched from readlink to basename.
#                     Updated read file names.
######################################################

##SCRIPT=$(readlink -f $0)
SCRIPT=`basename $0`
SCRIPT_PATH=$(dirname $SCRIPT)

. ${SCRIPT_PATH}/WLSenv-run.sh

${WL_HOME}/common/bin/wlst.sh -loadProperties ${SCRIPT_PATH}/WLSenv-run.properties ${SCRIPT_PATH}/startManagedServers.py