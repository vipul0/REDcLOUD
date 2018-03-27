#!/usr/bin/bash
cat << X >> /etc/samba/smb.conf
[try]
	path=\share\try
	hosts allow=192.168.1.102
	writable=yes
	valid users =vimal
	browseable=yes

X
exit