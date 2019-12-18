#!/usr/bin/env python

## This program receives encoder data from the /encoder_data topic
# and uses it to compute the robot's pose (x,y,theta) in the world
# frame. It then publishes a tf frame with the necessary transformation.
__author__ = "Rebecca Roembke, Victor Freire, Wanyue Xu"
__email__ = "freiremelgiz@wisc.edu"

# Dependencies
import rospy
import tf
import math
from latd.msg import enc_data

# Global variables
x_old=0
y_old=0
theta_old=0
encLeft_old=0
encRight_old=0

# Convert encoder data to pose
def enc_to_xyz(encLeft, encRight):
    global x_old
    global y_old
    global theta_old
    global encRight_old
    global encLeft_old
    # encLeft & encRight are number of ticks

    # Kinematic equations from ME439
    encRight_diff=encRight-encRight_old
    encLeft_diff=encLeft-encLeft_old
    delta_S_right=2*math.pi*0.03*encRight_diff/1440
    delta_S_left=2*math.pi*0.03*encLeft_diff/1440
    delta_S= (delta_S_left+delta_S_right)/2
    theta=theta_old-(delta_S_right-delta_S_left)/0.149
    x=x_old-delta_S*math.sin(theta_old+(theta/2))
    y=y_old+delta_S*math.cos(theta_old+(theta/2))

    # Shift register
    encRight_old=encRight
    encLeft_old=encLeft
    theta_old=theta
    x_old=x
    y_old=y

    # Return pose
    return [x, y, theta]

# Publish the transform tf
def get_pose(msg):
    pose = enc_to_xyz(msg.encLeft, msg.encRight)
    x = pose[0]
    y = pose[1]
    theta = pose[2]
    br = tf.TransformBroadcaster()
    br.sendTransform((x, y, 0),
                     tf.transformations.quaternion_from_euler(0, 0,theta),
                     rospy.Time.now(),
                     "robot",
                     "world")

if __name__ == '__main__':
    rospy.init_node('robot_frame_broadcaster')
    rospy.Subscriber('/encoder_data',enc_data , get_pose)
    rospy.spin()

