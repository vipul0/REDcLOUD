#!/usr/bin/bash
cat << X >> /etc/fstab
/dev/myvg/redhat-try   /home/redhat/try  ext4 defaults 0	0

X
exit