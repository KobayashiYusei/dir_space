#!/bin/bash
dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
colcon build
source $dir/.bashrc
timeout 30 ros2 run dir_space pub_node / > /tmp/dir_space.log
cat /tmp/dir_space.log | grep 'Free disk space'