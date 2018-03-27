#!/usr/bin/python2
import storage, commands

#dsize=cgi.FormContent()['osize'][0]
#cip=cgi.FormContent()['clientip'][0]
#fname=cgi.FormContent()['fnm'][0]

def mountlvm(PN,UN):
	SI, SP = storage.StorageDetail()
	if commands.getstatusoutput("sshpass -p {1} ssh -o stricthostkeychecking=no -l root {0}  mkdir -p  /object/{2}".format(SI, SP, PN))[0]==0:
		if commands.getstatusoutput("sshpass -p {1} ssh -o stricthostkeychecking=no -l root {0}  chmod o+w  /object/{2}".format(SI, SP, PN))[0]==0:
			if commands.getstatusoutput("sshpass -p {1} ssh -o stricthostkeychecking=no -l root {0}  mount /dev/myvg/{3}-{2} /home/{3}/{2} ".format(SI, SP, PN, UN))[0]==0:
				pass
			pass
		return 1;
	else:
		return 0;

def folderlist(UN):
	SI, SP=storage.StorageDetail()
	z=0
	for i in commands.getoutput("sshpass -p {1} ssh -o stricthostkeychecking=no -l root {0}  ls -l /home/{2}".format(SI,SP,UN)).split("\n"):
		if z<=1:
			z+=1
			pass
		else:
			nm=i.split()[8]
			size=i.split()[4]
			perm=i.split()[0]
			datapr="<tr><td><input value='"  + nm + "' type='button' onclick=openfold(this.value) />" "</td><td>" + size +"</td><td>" + perm +"</td><td>oo</td>"
			print datapr


def itemlist(fn,UN):
	SI, SP=storage.StorageDetail()
	z=0
	for i in commands.getoutput("sshpass -p {1} ssh -o stricthostkeychecking=no -l root {0}  ls -l /home/{3}/".format(SI,SP,fn,UN)).split("\n"):
		if z<=1:
			z+=1
			pass
		else:
			nm=i.split()[8]
			size=i.split()[4]
			perm=i.split()[0]
			datapr="<tr><td>" + nm + "</td><td>" + size +"</td><td>" + perm +"</td><td>oo</td>"
			print datapr



def ManageMatter(UN):
	SI, SP=storage.StorageDetail()
	for i in commands.getoutput("sshpass -p  {0} ssh -o stricthostkeychecking=no -l root {1} ls -l /object/{}".format(SP,SI,UN)).split("\n"):
		j=i.split()
		t=j[-1].split("/")
		datapr="<tr><td>" + t[2] + "</td><td>" + j[1] +"</td><td>" + j[2] +"</td><td></td><td>hai  </td><td><button onclick='myFunction()' >Dropdown</button></td></tr>"
		print datapr






def createlvm(S, PN, UN):
	SI, SP = storage.StorageDetail()
	z=commands.getstatusoutput("sshpass -p  {3} ssh -o stricthostkeychecking=no -l root {0} lvcreate --size {1}G  --name {4}-{2}  myvg ".format(SI,S,PN,SP,UN))
	if z[0]==0:
		return 1;
	else:
		return 0, z[1];


def formatlvm(typ, PN, UN):
	SI, SP = storage.StorageDetail()
	commands.getstatusoutput("sshpass -p {1} ssh -o stricthostkeychecking=no -l root {0}  mkfs.{2}  /dev/myvg/{4}-{3}".format(SI, SP, typ, PN,UN))


def mountlvm(PN,UN):
	SI, SP = storage.StorageDetail()
	if commands.getstatusoutput("sshpass -p {1} ssh -o stricthostkeychecking=no -l root {0}  mkdir -p  /home/{3}/{2}".format(SI, SP, PN,UN))[0]==0:
		if commands.getstatusoutput("sshpass -p {1} ssh -o stricthostkeychecking=no -l root {0}  chmod o+w  /home/{3}/{2}".format(SI, SP, PN,UN))[0]==0:
			if commands.getstatusoutput("sshpass -p {1} ssh -o stricthostkeychecking=no -l root {0}  mount /dev/myvg/{3}-{2} /home/{3}/{2} ".format(SI, SP, PN, UN))[0]==0:
				pass
			pass
		return 1;
	else:
		return 0;

def fstabentry(PN,UN):
	SI, SP=storage.StorageDetail()
	fstabString="#!/usr/bin/bash\ncat << X >> /etc/fstab\n/dev/myvg/{1}-{0}   /home/{1}/{0}  ext4 defaults 0	0\n\nX\nexit".format(PN,UN)
	f=open("/red/temp/stabentry.sh",'w')
	f.write(fstabString)
	f.close()
	commands.getoutput("sudo chmod +x /red/temp/stabentry.sh")
	if commands.getstatusoutput("sudo sshpass -p {0} scp /red/temp/stabentry.sh  root@{1}:/rundir/".format(SP, SI))[0]==0:
		filesta=commands.getstatusoutput("sshpass -p {0} ssh -o stricthostkeychecking=no -l root {1} bash /rundir/stabentry.sh ".format(SP, SI))
		commands.getoutput("sudo sshpass -p {0} ssh -o stricthostkeychecking=no -l root {1} rm -rf /rundir/stabentry.sh ".format(SP, SI))
		commands.getoutput("rm -rf /red/temp/stabentry.sh")
		return 1;
	else:
		return 0;

