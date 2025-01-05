#!/bin/bash
dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
colcon build
source $dir/.bashrc
timeout 10 ros2 run dir_space pub_node / > test_valid.log 2>&1 &
VALID_PID=$!
sleep 3
kill $VALID_PID
if grep -q "Publish disk space of /" test_valid.log; then
  echo "Valid path test passed."
else
  echo "Valid path test failed. Check test_valid.log."
  exit 1
fi

ros2 topic echo /dir_space