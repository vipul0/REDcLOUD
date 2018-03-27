#!/usr/bin/python2

import commands
import cgi

print "content-type: text/html"
print
print "\n\n"

#input
serverip="192.168.43.29"
serverpass="redhat"
name=cgi.FormContent()['osname'][0]
osvariant=cgi.FormContent()['osvariant'][0]
memory=cgi.FormContent()['osram'][0]
cpu=cgi.FormContent()['oscpu'][0]
port=cgi.FormContent()['osport'][0]

#software installation
status=commands.getstatusoutput("sudo sshpass -p {0} ssh -o stricthostkeychecking=no -l root {1} rpm -q qemu-kvm".format(serverpass,serverip))
if status[0]!=0:
    status1=commands.getstatusoutput("sudo sshpass -p {0} ssh -o stricthostkeychecking=no -l root {1} yum install qemu-kvm -y".format(serverpass,serverip))
    status2=commands.getstatusoutput("sudo sshpass -p {0} ssh -o stricthostkeychecking=no -l root {1} yum install virt-manager -y".format(serverpass,serverip))    
    if status2[0]!=0 or status1[0]!=0:
       print "Failed to install software in server side"
       exit()
else:
    print "software already installed"

status=commands.getstatusoutput("sudo sshpass -p {0} ssh -o stricthostkeychecking=no -l root {1} rpm -q virt-install".format(serverpass,serverip))
if status[0]==0:
    print "virt-install already installed" 
else:
    status1=commands.getstatusoutput("sudo sshpass -p {0} ssh -o stricthostkeychecking=no -l root {1} yum install virt-install".format(serverpass,serverip))
    if status1[0]!=0:
       exit()

#service start
status=commands.getstatusoutput("sudo sshpass -p {} ssh -o stricthostkeychecking=no -l root {} systemctl restart libvirtd".format(serverpass,serverip))
#configuration

status=commands.getstatusoutput("sshpass -p {6} ssh -o stricthostkeychecking=no -l root {7} sudo virt-install --name {0} --location /os/rhel-server-7.2-x86_64-dvd.iso --os-type {1} --os-variant {2} --memory {3} --vcpus {4} --disk /var/lib/libvirt/images/{0}.qcow2,size=7 --graphics vnc,listen=0.0.0.0,port={5} --noautoconsole".format(name,ostype,osvariant,memory,cpu,port,serverpass,serverip))

if status[0]==0:
    print "Virtual OS successfully started"
else:
    print "Virtual OS failed to start"
