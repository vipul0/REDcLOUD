#!/usr/bin/python2

#protocol used NFS PROTOCOL
#author VIPUL JAIN
#assume:
#1. vgwith name myvg exist
#2. sshpass, python, should be installed on server

#html file name is efs.html


print "content-type: text/html"
print
print "\n\n"
import cgi, os
import cloud

x=os.environ["HTTP_COOKIE"].split()
y=x[0].split("=")
userid=y[1]

#getting form field data
fname=cgi.FormContent()['fnm'][0]
dsize=cgi.FormContent()['psize'][0]

#create lvm
cloud.SshfsHandle.createlvm(dsize,fname,userid)

cloud.SshfsHandle.formatlvm("ext4",fname,userid)
#mount lvm" 
cloud.SshfsHandle.mountlvm(fname,userid)
#creating fstab entry
cloud.SshfsHandle.fstabentry(fname,userid)

print "location: s3.py"
print "\n\n"

exit()
