#!/usr/bin/python2


import cgi
import commands

print "content-type: text/html"

imageName=cgi.FormContent()['imagen'][0]
cName=cgi.FormContent()['cname'][0]


if commands.getstatusoutput("sudo docker inspect {0}".format(cName))[0]  == 0:
	print "\n\n"
	print "{} : this container name already exists".format(cName)

else:
	commands.getoutput("sudo docker run  -dit --name {0}  {1}".format(cName,imageName))
	print "location: caas.py"
	print "\n\n"





