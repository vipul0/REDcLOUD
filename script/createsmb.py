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

dsize=cgi.FormContent()['Ssize'][0]
bop=cgi.FormContent()['browseop'][0]
fname=cgi.FormContent()['fnm'][0]
Cip=cgi.FormContent()['cip'][0]

#create lvm
cloud.storage.createlvm(dsize,fname,userid)

#formatlvm
cloud.storage.formatlvm("ext4",fname,userid)

#mount lvm" 
cloud.storage.mountlvm(fname,userid)

#creating fstab entry
cloud.storage.fstabentry(fname,userid)

#Exports Entry
cloud.SmbHandle.Smbentry(fname, userid, Cip, bop)

#start the service
cloud.SmbHandle.SmbService()

print "location: smb.py"
print "\n\n"
