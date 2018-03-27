#!/usr/bin/python

import commands

def CheckingSupport(SI,SP):
	commands.getstatusoutput("sshpass -p {0} ssh -o stricthostkeychecking=no -l root {1} grep -i vmx /proc/cpuinfo".format(SP, SI))


def scsi(SI,SP):
	commands.getstatusoutput("sshpass -p {0} ssh -o stricthostkeychecking=no -l root {1} yum install libvirt qemu-kvm virt-manager virt-install -y".format(SP, SI))
	commands.getstatusoutput("sshpass -p {0} ssh -o stricthostkeychecking=no -l root {1} systemctl start libvirtd".format(SP, SI))
	commands.getstatusoutput("sshpass -p {0} ssh -o stricthostkeychecking=no -l root {1} systemctl enable libvirtd".format(SP, SI))



