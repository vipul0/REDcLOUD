#!/usr/bin/python2

import storage, commands

def Smbentry(FN, UN, CIP, B):
	SI, SP=storage.StorageDetail()
	fSMBstring="#!/usr/bin/bash\ncat << X >> /etc/samba/smb.conf\n[{0}]\n\tpath=\share\{0}\n\thosts allow={2}\n\twritable=yes\n\tvalid users ={1}\n\tbrowseable={3}\n\nX\nexit".format(FN, UN, CIP, B)
	f=open("/red/temp/fSMBentry.sh",'w')
	f.write(fSMBstring)
	f.close()
	commands.getoutput("sudo chmod +x /red/temp/fSMBentry.sh")
	if commands.getstatusoutput("sudo sshpass -p {0} scp /red/temp/fSMBentry.sh  root@{1}:/rundir/".format(SP,SI))[0]==0:
		filesta=commands.getstatusoutput("sudo sshpass -p {1} ssh -o stricthostkeychecking=no -l root {0} bash /rundir/fSMBentry.sh".format(SI,SP))
		commands.getstatusoutput("sudo sshpass -p {1} ssh -o stricthostkeychecking=no -l root {0} rm -rf /rundir/fSMBentry.sh".format(SI,SP))
		commands.getstatusoutput("sudo rf -rf /red/temp/fSMBentry.sh")
		return 1;
	else:
		return 0;


def SmbService():
	SI, SP=storage.StorageDetail()
	commands.getstatusoutput("sudo sshpass -p {0} ssh -o stricthostkeychecking=no -l root {1}  systemctl restart smb &".format(SP,SI))

