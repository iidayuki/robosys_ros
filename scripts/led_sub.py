#!/usr/bin/env python

import rospy
from std_msgs.msg import Bool

def led1_callback(msg):
	with open("/dev/myled0", "w") as f:
		f.write("1\n" if msg.data else "0\n")

def led2_callback(msg):
	with open("/dev/myled0", "w") as f:
		f.write("3\n" if msg.data else "2\n")

if __name__ == "__main__":
	rospy.init_node("led_flusher")
	sub1 = rospy.Subscriber("led1", Bool, led1_callback, queue_size=10)
	sub2 = rospy.Subscriber("led2", Bool, led2_callback, queue_size=10)
	rospy.spin()

