#!/usr/bin/python2

import commands

def rawcss():
	f=open("/red/script/assets/css/bootstrap.min.css",'r')
	x=f.read()
	f.close()
	f=open("/red/script/assets/css/main.css",'r')
	y=f.read()
	f.close()
	return x, y;


def rawjs():
	f=open("/red/script/assets/js/bootstrap.min.js",'r')
	x=f.read()
	f.close()
	return x;
