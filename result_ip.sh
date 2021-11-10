#!/bin/bash
#容器环境快速查IP
ifconfig eth0|awk 'NR==2 {print "IP="$2,"MASK="$4}'
