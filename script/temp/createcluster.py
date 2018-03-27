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

cname=cgi.FormContent()['clustername'][0]

f=open("/red/script/Hadoop/cluster.txt",'a')
f.write("{0}".format(cname))
f.close()

print "location: Hadoop1Cluster.py"
print "\n\n"
