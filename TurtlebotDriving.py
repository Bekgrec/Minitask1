#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist

def open_loop():
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    rospy.init_node('open_loop', anonymous=True)	
    rate = rospy.Rate(10)
    t0 = rospy.Time.now().to_sec()
    vel_info = Twist()

    vel_info.linear.x = 0
    vel_info.linear.y = 0
    vel_info.linear.z = 0
    vel_info.angular.x = 0
    vel_info.angular.y = 0
    vel_info.angular.z = 0

    while not rospy.is_shutdown():
        count = 0
        vel_info.linear.x = 0.5
 
        if count == 2:
            vel_info.linear.x = 0
            vel_info.angular.z = PI
            count = 0
        print(vel_info)
        pub.publish(vel_info)
        count += 1
 


if __name__ == '__main__':
    try:
        open_loop()
    except rospy.ROSInterruptException:
        pass





