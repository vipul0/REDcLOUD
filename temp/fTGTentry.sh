#!/usr/bin/bash
cat << X >> /etc/tgt/targets.conf
<target 1123>
backing-store /dev/myvg/vimal-try4
</target>
X
exit