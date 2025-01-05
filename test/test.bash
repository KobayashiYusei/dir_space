#!/bin/bash
dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
colcon build
source $dir/.bashrc
ros2 run dir_space pub_node / > test_valid.log 2>&1 & VALID_PID=$!
sleep 3
kill $VALID_PID
if grep -q "Publish disk space of /" test_valid.log; then
  exit 0
else
  echo "failed publish"
  exit 1
fi

ros2 run dir_space pub_node /dummy/path > test_invalid.log 2>&1 || true
if grep -q "path does not exist" test_invalid.log; then
  exit 0
else
  echo "faild invalid path test"
  exit 1
fi