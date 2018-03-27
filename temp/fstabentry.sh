#!/usr/bin/bash
cat << X >> /etc/fstab
/dev/myvg/vimal-data5   /home/vimal/data5  ext4 defaults 0	0
X
exit