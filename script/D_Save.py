#!/usr/bin/python2

import commands
import cgi

print "content-type: text/html"
  


cName=cgi.FormContent()['x'][0]


cimagestatus=commands.getstatusoutput("sudo docker commit {0}  {0}:v1".format(cName))


if cimagestatus[0]  == 0:
	print "location:  caas.py"
	print
else:
	print "not stoped"








