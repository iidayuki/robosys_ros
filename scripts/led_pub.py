#!/usr/bin/env python 

import rospy
from std_msgs.msg import Bool

if __name__ == "__main__":
	rospy.init_node("led_pub")
	pub1 = rospy.Publisher("led1", Bool, queue_size=10)
	pub2 = rospy.Publisher("led2", Bool, queue_size=10)
	rate = rospy.Rate(10)

	pub1.publish(False)
	pub2.publish(False)

	try:
		while not rospy.is_shutdown():
			direction = raw_input('a: Left, s: Duble, d: Right, q: None > ')
			if 'a' in direction:
				pub1.publish(True)
				pub2.publish(False)
			if 's' in direction:
				pub1.publish(True)
				pub2.publish(True)
			if 'd' in direction:
				pub1.publish(False)
				pub2.publish(True)
			if 'q' in direction:
				pub1.publish(False)
		                pub2.publish(False)
			
				rate.sleep()
	except rospy.KeybordInterrupt:
		pub1.publish(False)
                pub2.publish(False)
		pass
