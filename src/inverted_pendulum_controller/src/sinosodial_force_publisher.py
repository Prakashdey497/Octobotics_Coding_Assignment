#!/usr/bin/env python

import rospy
from inverted_pendulum_sim.msg import ControlForce
import numpy as np
import time


# Define the frequency, amplitude, and time parameters
frequency = 0.5  # Frequency in Hz
amplitude = 1.0  # Amplitude of the sinusoidal signal


def talker():
    rospy.init_node('force_publisher', anonymous=True)
    
    pub = rospy.Publisher('inverted_pendulum/control_force', ControlForce, queue_size=100)
    rate = rospy.Rate(100) # 10hz
    msg = ControlForce()
    while not rospy.is_shutdown():
        
        current_time = rospy.get_time()  # Get the current time
        force = amplitude * np.sin(2 * np.pi * frequency * current_time)
        
        # Create a ROS message with the signal value
        
        msg.force = force
        
        # Publish the message
        pub.publish(msg)
        
        # Sleep to maintain the desired publishing rate
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass