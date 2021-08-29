#!/usr/bin/env python

'''
* ROS Heartbeat broadcaster node *******************
 
 Publishes alive msgs to the Teensy microcontroller
 to tell that the computer is running.

****************************************************
'''

import rospy
from std_msgs.msg import Int16

def main():

    print "Initializing heartbeat_broadcaster..."

    # Publisher
    pub = rospy.Publisher('heartbeat', Int16, queue_size=10)

    msg = Int16()

    # Set up node
    rospy.init_node('heartbeat_broadcaster', anonymous=True)
    rate = rospy.Rate(10) # 10hz

    while not rospy.is_shutdown():

        msg.data = 1        
        pub.publish(msg)
        rate.sleep()


if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass