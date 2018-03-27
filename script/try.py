#!/usr/bin/python2
import cgi, os, extra, commands, cloud

print "Content-Type: text/html"

print "\n\n"

x=os.environ["HTTP_COOKIE"].split()
y=x[0].split("=")
userid=y[1]

print userid
