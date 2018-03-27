#!/usr/bin/bash
cat << X >> /etc/exports
/share/jolu 1237899(rw,sync,no_root_squash)
X
exit