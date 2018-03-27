#!/usr/bin/python2

import cgi
import commands

print "content-type: text/html"

cName=cgi.FormContent()['x'][0]
ip_address=commands.getoutput("sudo docker inspect {0} | jq '.[].NetworkSettings.IPAddress'".format(cName))
commands.getstatusoutput("sudo shellinaboxd -u root --port 6363 root -s :/SSH:{0} -t ".format(ip_address))
print "location 192.168.1.104:6363"
print "\n\n"

