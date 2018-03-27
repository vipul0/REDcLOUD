#!/usr/bin/python

import commands, infrastructure

SI, SP=infrastructure.IaasDetail()


def createimage(n,os,ov,m,c,p):
	if commands.getstatusoutput("sshpass -p {6} ssh -o stricthostkeychecking=no -l root {7} sudo virt-install --name {0} --location /os/rhel-server-7.3-x86_64-dvd.iso --os-type {1} --os-variant {2} --memory {3} --vcpus {4} --disk /var/lib/libvirt/images/{0}.qcow2,size=7 --graphics vnc,listen=0.0.0.0,port={5} --noautoconsole".format(name,ostype,osvariant,memory,cpu,port,SP,SI))[0]==0:




