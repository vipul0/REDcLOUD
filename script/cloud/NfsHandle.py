#!/usr/bin/python2
import storage, commands

#dsize=cgi.FormContent()['osize'][0]
#cip=cgi.FormContent()['clientip'][0]
#fname=cgi.FormContent()['fnm'][0]

def exportsentry(PN, CIP):
	SI, SP=storage.StorageDetail()
	fstabString="#!/usr/bin/bash\ncat << X >> /etc/exports\n/share/{0} {1}(rw,sync,no_root_squash)\nX\nexit".format(PN, CIP)
	f=open("/red/temp/ExportEntry.sh",'w')
	f.write(fstabString)
	f.close()
	commands.getoutput("chmod +x /red/temp/ExportEntry.sh")
	if commands.getstatusoutput("sudo sshpass -p {0} scp /red/temp/ExportEntry.sh  root@{1}:/rundir/ ".format(SP, SI))[0]==0:
		filesta=commands.getstatusoutput("sshpass -p {1} ssh -o stricthostkeychecking=no -l root {0} bash /rundir/ExportEntry.sh ".format(SI,SP))
		commands.getstatusoutput("sshpass -p {0} ssh -o stricthostkeychecking=no -l root {1} rm -rf /rundir/ExportEntry.sh ".format(SP, SI))
		return 1;
	else:
		return 0;

def exportremove():
	SI, SP=storage.StorageDetail()
	


def nfsservice():
	SI, SP=storage.StorageDetail()
	commands.getstatusoutput("sudo sshpass -p {0} ssh -o stricthostkeychecking=no -l root {1}  systemctl restart nfs".format(SP, SI))


def ManageMatter(UN):
	SI, SP=storage.StorageDetail()
	z=1
	for i in commands.getoutput("sshpass -p  {0} ssh -o stricthostkeychecking=no -l root {1} df -h | grep {2}".format(SP,SI,UN)).split("\n"):
		if z==1:
			z+=1
			pass
		else:
			j=i.split()
			t=j[-1].split("/")
			print j
			for u in commands.getoutput("sshpass -p  {0} ssh -o stricthostkeychecking=no -l root {1} cat /etc/exports | grep {2}".format(SP,SI,t[2])).split("\n"):
				if z<=2:
					z+=1
					pass
				else:
					y=u.split()[1].split("(")
					datapr="<tr><td>" + t[2] + "</td><td>" + j[1] +"</td><td>" + j[2] +"</td><td>" + y[0] + "</td><td> (" + y[1] + "</td><td>hai</td>"
					print datapr
