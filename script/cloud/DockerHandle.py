#!/usr/bin/python

import commands

def Content():
	z=1
	for i in commands.getoutput('sudo docker ps -a').split('\n'):
		if z==1:
			z=z+1
			pass
		else:
			j=i.split()
			con_status=commands.getoutput("sudo docker inspect {0} | jq '.[].State.Status'".format(j[-1]))
			ip_address=commands.getoutput("sudo docker inspect {0} | jq '.[].NetworkSettings.IPAddress'".format(j[-1]))
			print "<tr><td>" + j[1] + "</td><td>" + j[-1] + "</td><td>" + ip_address + "</td><td>" + con_status + "</td><td><input value='" + j[-1] + "'type='button' onclick=dock_start(this.value) /> " + "</td><td><input value='" + j[-1] + "'type='button' onclick=dock_stop(this.value) />" + "</td><td><input value='" + j[-1] + "'type='button' onclick=dock_remove(this.value) /></td><td><input value='" + j[-1] + "'type='button' onclick=dock_pause(this.value) /></td><td><input value='" + j[-1] + "'type='button' onclick=dock_unpause(this.value) />" + "</td><td><input value='" + j[-1] + "'type='button' onclick=dock_shell(this.value) />" + "</td><td><input value='" + j[-1] + "'type='button' onclick=dock_save(this.value) />" + "</td></tr>"




