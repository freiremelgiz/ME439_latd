#!/usr/bin/env python

## This program subscribes to /key_vel topic to read Twist messages
# An if-else function sets the motor speeds based on these messages
__author__ = "Victor Freire, Rebecca Roembke, Wanyue Xu"
__email__ = "freiremelgiz@wisc.edu"

# Dependencies
import rospy
from pololu_drv8835_rpi import motors
from geometry_msgs.msg import Twist

## INIT Objects
# Initialize node
rospy.init_node('driver', anonymous=False)

## Read the state of the keyboard and set motor speed
# "Arcade" driving
def set_speed(msg):
    if(msg.linear.x == 5.0):
        motors.motor1.setSpeed(-200)
        motors.motor2.setSpeed(200)
    elif(msg.linear.x == -5.0):
        motors.motor1.setSpeed(200)
        motors.motor2.setSpeed(-200)
    elif(msg.angular.z == -1.0):
        motors.motor1.setSpeed(150)
        motors.motor2.setSpeed(150)
    elif(msg.angular.z == 1.0):
        motors.motor1.setSpeed(-150)
        motors.motor2.setSpeed(-150)
    else:
        motors.motor1.setSpeed(0)
        motors.motor2.setSpeed(0)


# Listens Twist data continuously when called
def listener():
    # Create Subscriber for drive commands
    sub = rospy.Subscriber('/key_vel', Twist, set_speed)
    rospy.spin()

if __name__ == '__main__':
    try:
        listener()
    except rospy.ROSInterruptException:
        # Stop motors on error
        motors.motor1.setSpeed(0)
        motors.motor2.setSpeed(0)
        pass
