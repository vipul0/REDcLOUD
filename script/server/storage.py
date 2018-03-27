#!/usr/bin/python
import commands

def nfs(SI,SP):
	commands.getstatusoutput("sshpass -p {0} ssh -o stricthostkeychecking=no -l root {1} yum install nfs-utils -y".format(SP, SI))
	commands.getstatusoutput("sshpass -p {0} ssh -o stricthostkeychecking=no -l root {1} systemctl start nfs".format(SP, SI))
	commands.getstatusoutput("sshpass -p {0} ssh -o stricthostkeychecking=no -l root {1} systemctl start rpcbind".format(SP, SI))
	commands.getstatusoutput("sshpass -p {0} ssh -o stricthostkeychecking=no -l root {1} systemctl enable nfs".format(SP, SI))
	commands.getstatusoutput("sshpass -p {0} ssh -o stricthostkeychecking=no -l root {1} systemctl enable rpcbind".format(SP, SI))



def samba(SI,SP):
	commands.getstatusoutput("sshpass -p {0} ssh -o stricthostkeychecking=no -l root {1} yum install samba* -y".format(SP, SI))
	commands.getstatusoutput("sshpass -p {0} ssh -o stricthostkeychecking=no -l root {1} systemctl start smb".format(SP, SI))
	commands.getstatusoutput("sshpass -p {0} ssh -o stricthostkeychecking=no -l root {1} systemctl enable smb".format(SP, SI))



def scsi(SI,SP):
	commands.getstatusoutput("sshpass -p {0} ssh -o stricthostkeychecking=no -l root {1} yum install scsi-target-utils -y".format(SP, SI))
	commands.getstatusoutput("sshpass -p {0} ssh -o stricthostkeychecking=no -l root {1} systemctl start tgtd".format(SP, SI))
	commands.getstatusoutput("sshpass -p {0} ssh -o stricthostkeychecking=no -l root {1} systemctl enable tgtd".format(SP, SI))



