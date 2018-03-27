#!/usr/bin/python

import cgi, commands

print "content-type: text/html"

usern=cgi.FormContent()['uname'][0]
passkey=cgi.FormContent()['psw'][0]

if usern=="admin" and passkey=="hakim":
	print "location: ../admin.html"
	print "\n\n"
	exit()
elif commands.getstatusoutput("sudo id {0}".format(usern))[0]==0:
	print "location: Home.py"
	print "set-cookie: uname={}".format(usern)
	print "\n\n"
	exit()
else:
	print "location: ../create.html"
	print "\n\n"
	exit()
