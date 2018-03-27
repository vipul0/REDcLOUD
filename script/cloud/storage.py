#!/usr/bin/pyhton2
import commands

def StorageDetail():
	f=open("/red/config/storage.txt",'r')
	x=f.readlines()
	rawx=x[0].strip('\n')
	rawy=x[1].strip('\n')
	servIp=rawx.split(':')[1]
	servPass=rawy.split(':')[1]
	return servIp, servPass;




def createlvm(S, PN, UN):
	SI, SP = StorageDetail()
	z=commands.getstatusoutput("sshpass -p  {3} ssh -o stricthostkeychecking=no -l root {0} lvcreate --size {1}G  --name {4}-{2}  myvg ".format(SI,S,PN,SP,UN))
	if z[0]==0:
		return 1;
	else:
		return 0, z[1];


def snaplvm(S, PN):
	SI, SP = StorageDetail()
	z=commands.getstatusoutput("sshpass -p  {3} ssh -o stricthostkeychecking=no -l root {0} lvcreate -s --name {} --size {} ".format(SI,S,PN,SP))




def formatlvm(typ, PN, UN):
	SI, SP = StorageDetail()
	commands.getstatusoutput("sshpass -p {1} ssh -o stricthostkeychecking=no -l root {0}  mkfs.{2}  /dev/myvg/{4}-{3}".format(SI, SP, typ, PN,UN))


def extendlvm(typ, PN, UN):
	SI, SP = StorageDetail()
	commands.getstatusoutput("sshpass -p {1} ssh -o stricthostkeychecking=no -l root {0}  lvextend --size +{} /dev/myvg/{}".format(SI, SP,))
	commands.getstatusoutput("sshpass -p {1} ssh -o stricthostkeychecking=no -l root {0}  resize2fs /de/myvg/{}".format(SI, SP,))


def reducelvm(typ, PN, UN):
	SI, SP = StorageDetail()
	commands.getstatusoutput("sshpass -p {1} ssh -o stricthostkeychecking=no -l root {0}  umount /dev/myvg/{}".format(SI, SP,))
	commands.getstatusoutput("sshpass -p {1} ssh -o stricthostkeychecking=no -l root {0}  e2fsck -f /dev/myvg/{}".format(SI, SP,))
	commands.getstatusoutput("sshpass -p {1} ssh -o stricthostkeychecking=no -l root {0}  resize2fs /dev/myvg/{} {}".format(SI, SP,))
	commands.getstatusoutput("sshpass -p {1} ssh -o stricthostkeychecking=no -l root {0}  lvreduce --size {} /dev/myvg/{}".format(SI, SP,))
	commands.getstatusoutput("sshpass -p {1} ssh -o stricthostkeychecking=no -l root {0}  mount /dev/myvg/{} /share/{}".format(SI, SP,))



def mountlvm(PN,UN):
	SI, SP = StorageDetail()
	if commands.getstatusoutput("sshpass -p {1} ssh -o stricthostkeychecking=no -l root {0}  mkdir -p  /share/{2}".format(SI, SP, PN))[0]==0:
		if commands.getstatusoutput("sshpass -p {1} ssh -o stricthostkeychecking=no -l root {0}  chmod o+w  /share/{2}".format(SI, SP, PN))[0]==0:
			if commands.getstatusoutput("sshpass -p {1} ssh -o stricthostkeychecking=no -l root {0}  mount /dev/myvg/{3}-{2} /share/{2} ".format(SI, SP, PN, UN))[0]==0:
				pass
			pass
		return 1;
	else:
		return 0;


def deletelvm(UN,PN):
	SI, SP = StorageDetail()
	commands.getstatusoutput("sshpass -p {1} ssh -o stricthostkeychecking=no -l root {0} lvremove /dev/myvg/{3}-{2} -y".format(SI, SP, PN, UN))
	return 1;


def fstabentry(PN,UN):
	SI, SP=StorageDetail()
	fstabString="#!/usr/bin/bash\ncat << X >> /etc/fstab\n/dev/myvg/{1}-{0}   /share/{0}  ext4 defaults 0	0\nX\nexit".format(PN,UN)
	f=open("/red/temp/fstabentry.sh",'w')
	f.write(fstabString)
	f.close()
	commands.getoutput("chmod +x /red/temp/fstabentry.sh")
	if commands.getstatusoutput("sudo sshpass -p {0} scp /red/temp/fstabentry.sh  root@{1}:/rundir/".format(SP, SI))[0]==0:
		filesta=commands.getstatusoutput("sshpass -p {0} ssh -o stricthostkeychecking=no -l root {1} bash /rundir/fstabentry.sh ".format(SP, SI))
		commands.getoutput("sshpass -p {0} ssh -o stricthostkeychecking=no -l root {1} rm -rf /rundir/fstabentry.sh ".format(SP, SI))
		commands.getoutput("rm -rf /red/temp/fstabentry.sh")
		return 1;
	else:
		return 0;



