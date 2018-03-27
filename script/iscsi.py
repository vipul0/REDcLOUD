#!/usr/bin/python2

#protocol used ISCSI PROTOCOL
#author VIPUL JAIN
#assume:

#1. vgwith name myvg exist
#2. sshpass, python, should be installed on server

print "content-type: text/html"

import commands, cloud, os
import cgi

x=os.environ["HTTP_COOKIE"].split()
y=x[0].split("=")
userid=y[1]

#getting form field data
dsize=cgi.FormContent()['Bsize'][0]
fname=cgi.FormContent()['fnm'][0]
idn=cgi.FormContent()['idnm'][0]

#create lvm
cloud.storage.createlvm(dsize,fname,userid)

#create tgt entry
a=cloud.ScsiHandle.tgtentry(userid, fname, idn)

#restart the service
cloud.ScsiHandle.ScsiService()

print "location: ebs.py"
print "\n\n\n"
