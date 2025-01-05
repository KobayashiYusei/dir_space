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

# Launch the node in the background
echo "Launching pub_node..."
timeout 10 ros2 run dir_space pub_node &
NODE_PID=$!

# Wait a moment to ensure the node is running
sleep 2

# Check if the topic is publishing data
echo "Checking if data is being published on /dir_space..."
timeout 5 ros2 topic echo /dir_space > test_topic.log &
ECHO_PID=$!

# Wait for the echo to finish or timeout
sleep 6

# Terminate background processes
kill -9 $NODE_PID || true
kill -9 $ECHO_PID || true

# Check if any data was published
if grep -q "data:" test_topic.log; then
  echo "Topic test passed. Data is being published on /dir_space."
  rm -f test_topic.log
  exit 0
else
  echo "Topic test failed. No data was published on /dir_space."
  rm -f test_topic.log
  exit 1
fi