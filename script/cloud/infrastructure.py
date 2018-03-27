#!/usr/bin/python2

def IaasDetail():
	f=open("/red/config/iaas.txt",'r')
	x=f.readlines()
	rawx=x[0].strip('\n')
	rawy=x[1].strip('\n')
	servIp=rawx.split(':')[1]
	servPass=rawy.split(':')[1]
	return servIp, servPass;


