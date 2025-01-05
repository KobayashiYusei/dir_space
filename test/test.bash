#!/bin/bash
# SPDX-FileCopyrightText: 2024 Kobayashi Yusei
# SPDX-License-Identifier: BSD-3-Clause
# See LICENSE file for more details.
dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
colcon build
source $dir/.bashrc
ros2 run dir_space pub_node / > test_publish.log 2>&1 & PUB_PID=$!
sleep 3
kill $PUB_PID
if grep -q "Publish disk space of /" test_publish.log; then
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

timeout 10 ros2 run dir_space pub_node & NODE_PID=$!
sleep 6
timeout 10 ros2 topic echo /dir_space > test_topic.log & LISTEN_PID=$!
sleep 6
kill -SIGKILL $NODE_PID || true
kill -SIGKILL $LISTEN_PID || true

if grep -q "data:" test_topic.log; then
  exit 0
else
  exit 1
rm -rf test_topic.log
fi