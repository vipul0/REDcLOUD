#!/usr/bin/python2
import storage, commands

def tgtentry(UN, FN, IDN):
	SI, SP=storage.StorageDetail()
	fTGTstring="#!/usr/bin/bash\ncat << X >> /etc/tgt/targets.conf\n<target {1}>\nbacking-store /dev/myvg/{2}-{0}\n</target>\nX\nexit".format(FN, IDN, UN)
	f=open("/red/temp/fTGTentry.sh",'w')
	f.write(fTGTstring)
	f.close()
	commands.getstatusoutput("chmod +x /red/temp/fTGTentry.sh")
	if commands.getstatusoutput("sudo sshpass -p {0} scp /red/temp/fTGTentry.sh  root@{1}:/rundir/".format(SP,SI))[0]==0:
		filesta=commands.getstatusoutput("sudo sshpass -p {1} ssh -o stricthostkeychecking=no -l root {0} bash /rundir/fTGTentry.sh".format(SI,SP))
		commands.getstatusoutput("sudo sshpass -p {1} ssh -o stricthostkeychecking=no -l root {0} rm -rf /rundir/fTGTentry.sh".format(SI,SP))
		commands.getstatusoutput("rf -rf /red/temp/fTGTentry.sh")
		return 1;
	else:
		return 0;



def ScsiService():
	SI, SP=storage.StorageDetail()
	commands.getstatusoutput("sudo sshpass -p {0} ssh -o stricthostkeychecking=no -l root {1}  systemctl restart tgtd &".format(SP,SI))



def ManageMatter():
	SI, SP=storage.StorageDetail()
	z=1
	tgtid=[]
	tgtname=[]
	for i in commands.getoutput("sshpass -p  {0} ssh -o stricthostkeychecking=no -l root {1} cat /etc/tgt/targets.conf | grep target ".format(SP,SI)).split("\n"):
		if i=="</target>":
			pass
		else:
			tgtid.append(i.split(" ")[1])
	for j in commands.getoutput("sshpass -p  {0} ssh -o stricthostkeychecking=no -l root {1} cat /etc/tgt/targets.conf | grep backing ".format(SP,SI)).split("\n"):
		tgtname.append(j.split(" ")[1])
	for i in range(len(tgtid)):
		datapr="<tr><td>" + tgtname[i] + "<td> -* </td><td> -* </td></td><td>" + tgtid[i].rstrip(">") +"</td><td> -* </td>"
		print datapr
