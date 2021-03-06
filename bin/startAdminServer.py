######################################################
# NAME: startAdminServer.py
#
# DESC: Starts Oracle WebLogic Server (WLS) domain Administration Server.
#       Note that the file ${DOMAIN_HOME}/servers/${ADMIN_SERVER_NAME}/security/boot.properties
#       must exist in order to start a server with nmStart.
#
# $HeadURL:  $
# $LastChangedBy: $
# $LastChangedDate: $
# $LastChangedRevision: $
#
# LOG:
# yyyy/mm/dd [user] - [notes]
# 2014/01/17 cgwong - [v1.0.0] Creation.
# 2014/03/19 cgwong - [v1.1.0] Switched node manager connection to use
#                     user store and key file syntax for improved security.
#                     Updated header comments.
# 2014/03/20 cgwong - [v1.1.1] Updated cfg_home and fmw_home variables.
######################################################

import socket;
nm_listen_address = socket.gethostname();

print 'CREATE PATHS';
domain_name = os.getenv('DOMAIN_NAME');
java_home = os.getenv('JAVA_HOME');
mw_home = os.getenv('MW_HOME');
wls_home = os.getenv('WL_HOME');
fmw_home = os.getenv('FMW_HOME');
cfg_home = os.getenv('CFG_BASE');

domain_home = cfg_home + '/domains/' + domain_name;
domain_application_home = cfg_home + '/webapps/' + domain_name;
nm_home = domain_home + '/nodemanager';

print 'CONNECT TO NODE MANAGER';
##nmConnect(nm_username, nm_password, nm_listen_address, nm_listen_port, domain_name, domain_home, nm_mode);
nmConnect(userConfigFile=domain_home + nm_cfg_file, userKeyFile=domain_home + nm_key_file, host=nm_listen_address, port=nm_listen_port, domainName=domain_name, domainDir=domain_home, nmType=nm_mode);

print 'START ADMIN SERVER';
nmStart(aserver_name);

print 'DISCONNECT FROM NODE MANAGER';
nmDisconnect();
