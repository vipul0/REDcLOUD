#!/usr/bin/python2

#protocol used NFS PROTOCOL
#author VIPUL JAIN
#assume:
#1. vgwith name myvg exist
#2. sshpass, python, should be installed on server

#html file name is efs.html


print "content-type: text/html"
import cgi, os
import cloud

x=os.environ["HTTP_COOKIE"].split()
y=x[0].split("=")
userid=y[1]

#getting form field data
fname=cgi.FormContent()['fnm'][0]

#intial size is of 2gb
dsize=2
#create lvm
a=cloud.storage.createlvm(dsize,fname,userid)

#formatlvm
b=cloud.storage.formatlvm(ftype,fname,userid)

#mount lvm" 
c=cloud.S3Handle.mountlvm(fname,userid)

#creating fstab entry
d=cloud.storage.fstabentry(fname,userid)

if a==1:
	print "location: efs.py"
	print "\n\n"
	exit()
else:
	print "\n\n"
	print "some error" + str(a)
