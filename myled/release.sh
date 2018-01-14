#!/bin/bash -eu

echo 0 > /dev/myled0
sudo rmmod myled
make clean

chmod -x myled.c
chmod -x ~/catkin_ws/src/robosys_ros/scripts/led_sub.py
chmod -x ~/catkin_ws/src/robosys_ros/scripts/led_pub.py


