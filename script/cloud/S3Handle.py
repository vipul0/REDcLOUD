#!/usr/bin/python2
import storage, commands

#dsize=cgi.FormContent()['osize'][0]
#cip=cgi.FormContent()['clientip'][0]
#fname=cgi.FormContent()['fnm'][0]

def mountlvm(PN,UN):
	SI, SP = StorageDetail()
	if commands.getstatusoutput("sshpass -p {1} ssh -o stricthostkeychecking=no -l root {0}  mkdir -p  /object/{2}".format(SI, SP, PN))[0]==0:
		if commands.getstatusoutput("sshpass -p {1} ssh -o stricthostkeychecking=no -l root {0}  chmod o+w  /object/{2}".format(SI, SP, PN))[0]==0:
			if commands.getstatusoutput("sshpass -p {1} ssh -o stricthostkeychecking=no -l root {0}  mount /dev/myvg/{3}-{2} /object/{2} ".format(SI, SP, PN, UN))[0]==0:
				pass
			pass
		return 1;
	else:
		return 0;

def folderlist():
	SI, SP=storage.StorageDetail()
	z=0
	for i in commands.getoutput("sshpass -p {1} ssh -o stricthostkeychecking=no -l root {0}  ls -l /object".format(SI,SP)).split("\n"):
		if z<=1:
			z+=1
			pass
		else:
			nm=i.split()[8]
			size=i.split()[4]
			perm=i.split()[0]
			datapr="<tr><td>" + nm + "</td><td>" + size +"</td><td>" + perm +"</td><td>oo</td>"
			print datapr


def itemlist(fn):
	SI, SP=storage.StorageDetail()
	z=0
	for i in commands.getoutput("sshpass -p {1} ssh -o stricthostkeychecking=no -l root {0}  ls -l /object/{}".format(SI,SP,fn)).split("\n"):
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
