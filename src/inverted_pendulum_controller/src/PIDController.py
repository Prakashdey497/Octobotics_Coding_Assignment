#!/usr/bin/env python
import rospy
import numpy as np
import math
from inverted_pendulum_sim.msg import CurrentState
from inverted_pendulum_sim.msg import ControlForce


class PIDControll():
    def __init__(self,kp=1.0,kd=0.0,ki = 0.0,gravity = 9.8):
        # The gains were emperically tuned
        self.Kp = kp
        self.Kd = kd
        self.Ki = ki
        
        self.previous_error = 0
        self.integral = 0
        self.gravity = gravity
        
        self.previous_timestamp = rospy.get_time()
        self.message = ControlForce()
        
        self.current_state_sub = rospy.Subscriber('/inverted_pendulum/current_state', CurrentState, self.PIDControll_callback)
        self.ctrl_force_pub = rospy.Publisher('/inverted_pendulum/control_force', ControlForce, queue_size=10)
        
        self.previous_time_delta = 0
        
    def PIDControll_callback(self,msg):
        current_timestamp = rospy.get_time()
        time_delta = (current_timestamp - self.previous_timestamp)
        error = self.find_error(msg.curr_theta)
        if self.previous_time_delta != 0:	# This condition is to make sure that theta_dot is not infinity in the first step
            
            F = self.find_pid_control_input(time_delta,error,self.previous_error,self.gravity)
            self.message.force = F
            self.ctrl_force_pub.publish(self.message)
            
        self.previous_time_delta = time_delta
        self.previous_timestamp = current_timestamp
        self.previous_error = error
        
    
    
    def find_error(self,pendulum_angle):
        previous_error = (pendulum_angle % (2 * math.pi)) - 0
        if previous_error > math.pi:
            previous_error = previous_error - (2 * math.pi)
        return previous_error


    def find_pid_control_input(self,time_delta,error,previous_error,g):
        
        # Proportional term
        P = self.Kp * error
        
        # Integral term
        self.integral += error * time_delta
        I = self.Ki * self.integral
        
        # Derivative term
        derivative = (error - previous_error)/ time_delta
        D = self.Kd * derivative
        
        # Calculate the control input
        control_input = P + I + D
        
        return control_input
    
    
if __name__== '__main__':
    rospy.init_node('PID_Cotrol', anonymous=True)
    node = PIDControll()
    rospy.spin()
    