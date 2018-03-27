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

dsize=cgi.FormContent()['osize'][0]
ftype=cgi.FormContent()['ty'][0]
fname=cgi.FormContent()['fnm'][0]
Cip=cgi.FormContent()['cip'][0]

#create lvm
a=cloud.storage.createlvm(dsize,fname,userid)

#formatlvm
b=cloud.storage.formatlvm(ftype,fname,userid)

#mount lvm" 
c=cloud.storage.mountlvm(fname,userid)

#creating fstab entry
d=cloud.storage.fstabentry(fname,userid)

#Exports Entry
cloud.NfsHandle.exportsentry(fname, Cip)

#start the service
e=cloud.NfsHandle.nfsservice()


if a==1:
	print "location: efs.py"
	print "\n\n"
	exit()
else:
	print "\n\n"
	print "some error" + str(a)
